import json, configparser, subprocess, sys, time, threading

try:
    import websocket
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'websocket-client'])
    import websocket

try:
    from discord_webhook import DiscordWebhook
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord-webhook'])
    from discord_webhook import DiscordWebhook

try:
    from google_trans_new import google_translator
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'google-trans-new'])
    from google_trans_new import google_translator

translator = google_translator()
config = configparser.ConfigParser()
config.read('config.ini')

ping_interval = 30

def on_message(ws, response):
    if 'chatpush' in response:
        chat_info = json.loads(response[2:])[1]
        user_info = json.loads(chat_info['fp'])
        user = user_info['username']
        message = chat_info['content']
        message = str(translator.translate(chat_info['content']))
        
        channel = ''
        for key in list(config['topwar_channels'].keys()):
            if chat_info['roomId'] == config['topwar_channels'][key]:
                channel = f'**[{key}]**'

        alliance = ''
        if chat_info['fat']:
            alliance = '**[%s]** ' % chat_info['fat']
        
        for key in list(config['discord_webhooks'].keys()):
            DiscordWebhook(url=config['discord_webhooks'][key], content=f'{channel}{alliance}{user}: {message}').execute()
    elif 'pingInterval' in response:
        server_config = json.loads(response[1:])
        ping_interval = server_config['pingInterval'] / 60

def on_close(ws):
    print('disconnected')

def on_open(ws):
    print('connection established')

    count = 420
    for key in list(config['topwar_channels'].keys()):
        print(f'Joined {key}')
        ws.send('{}["join","{}"]'.format(count, config['topwar_channels'][key]))
        count += 1

    print('Binded UUID: %s' % config['topwar']['uuid'])
    ws.send('{}["bind","{}"]'.format(count, config['topwar']['uuid']))

    def start_heartbeat():
        time.sleep(ping_interval)
        ws.send('2')
        start_heartbeat()
    
    threading.Thread(target=start_heartbeat).start()


def connect_websocket():
    ws = websocket.WebSocketApp(config['topwar']['websocket'],
        on_message=on_message,
        on_close=on_close,
        on_open=on_open)
    ws.run_forever()

if __name__ == '__main__':
    connect_websocket()