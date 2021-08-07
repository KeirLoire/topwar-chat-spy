## Section A. How do I get the websocket of the game?

I used a packet listening tool called HttpCanary, that's where I discovered that the game is using websockets. Not the best approach but you get the idea.

1. Install HttpCanary app.

2. Open HttpCanary.

3. Install Parallel Space (including the 64-bit) from HttpCanary Settings.

4. Add Parallel Space (including the 64-bit) to Target Apps from HttpCanary.

5. Go to the Filter menu from the top-right button, then select WebSocket under Protocols.

6. Press the blue floating button from the bottom-right to start capturing.

7. Once HttpCanary has started capturing, it will minimize into a small box. Don't close it.

8. Open Parallel Space.

9. Add Top War to Parallel Space.

10. Open Top War in Parallel Space.

11. Once the game has loaded, HttpCanary will show logs containing the websockets.

12. Go back to HttpCanary by pressing the white box.

12. Press the green floating button from the bottom-right to stop capturing.

13. HttpCanary will show two websockets.
    - The first one is the `chat websocket`.
        - This websocket is for receiving chats in the game.
        - From my side, the chat websocket URL is:
          - wss://group-push-us.rivergame.net/socket.io/sjzb/721?EIO=3&transport=websocket
    - The second one is the `game websocket` which is encoded in binary format.
        - This websocket is used for interacting in the game.
        - From my side, the game websocket URL is:
          - wss://knight-us-gcp-1400.topwargame.com/s721

<img src="https://github.com/KeirLoire/topwar-discord-chat/blob/main/img/httpcanary_websockets.jpg?raw=true" width="500"/><br>

## Section B. How do I get the world chat ID and alliance ID of the game?

You might wanna to change the account used in Top War Parallel Space then repeat the packet listening steps from Section A.

### From the chat websocket (Get current world ID and alliance ID from your account).

1. Press the `chat websocket` from HttpCanary.

2. Refer to the image below for getting the alliance ID.

<img src="https://github.com/KeirLoire/topwar-discord-chat/blob/main/img/httpcanary_chat_websocket.jpg?raw=true" width="500"/><br>

### From the game websocket (Get alliance ID from alliance ranking list).

I know, this method is bad, there must be a better way to send/listen to these websockets.

1. Clear the logs from HttpCanary.

2. Start capturing from HttpCanary. 

3. Open Top War from Parallel Space.

4. Go to Alliance Ranking.

5. Scroll down until you find the alliance that you want to get the ID of.

6. Go back to HttpCanary and stop capturing.

7. Press the `game websocket`.

8. Save the log for `game websocket`.

9. Transfer the saved logs or the BIN files into PC.

10. Extract all BIN files using 7-Zip. (some files may fail to extract, not sure why?)

11. Open an Editing Tool to the directory where the files are extracted.
    - Visual Code or something similar that is capable of searching through multiple files.

12. Search for files containing `"c":651`. (this is the action for getting alliance rank list)

13. Once you find the file that is containing `"c":651`, you now have the file containing the alliance rank list with their IDs.

14. The `aid` is the alliance ID which you can't use in the script yet. You need to change the format into this first:
    - Format:
        - 102_2_<server_number>_<alliance_id>
    - Examples:
        - 102_2_691_385492
        - 102_2_691_406558

For a better view of the file:
- Remove unnecessary characters.
  - Search `\"` then replace it to `"`
  - Search `"d":"` then replace it to `"d":`
  - Search `","o"` then replace it to `,"o"`
- Copy the content then open it on a JSON viewer tool.

<img src="https://github.com/KeirLoire/topwar-discord-chat/blob/main/img/websocket_action_651.png?raw=true"/><br>