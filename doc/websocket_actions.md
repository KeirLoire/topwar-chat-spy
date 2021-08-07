## About

My findings on interacting in the game via websockets. Potentially, you could develop a bot for the game that you could simly control by issuing commands from Discord or automate some stuff.

### STANDARD WEBSOCKET FORMAT
```json
{"c":<action>,"o":"<count>","p":{}}
```

### 1134 - Get alliance list
```json
{"c":1134,"o":"177","p":{}}
```

### 861 - Get hero list
```json
{"c":861,"o":"4","p":{}}
```

### 933 - Get mail list
```json
{"c":933,"o":"197","p":{"mailGroupType":3,"mailId":"","limitCount":49}}
```

### 670 - Send chat
```json
{"c":670,"o":"165","p":{"c":0,"m":":3","uid":"","llm":"","custom":"{"mod":"","modPic":0,"officialTitle":-1}","group":""}}
```


### 670 - Send chat with link, in-game emoji, or coordinates.
```json
{"c":670,"o":"219","p":{"c":0,"m":"link25","uid":"","llm":"{"t":2,"emotionId":25,"iconIDs":"25","iconID":25,"uts":1}","custom":"{"mod":"","modPic":0,"officialTitle":-1}","group":""}}
```

### 901 - Get map info
```json
{"c":901,"o":"242","p":{"x":508,"y":384,"k":1037,"width":7,"height":16,"marchInfo":true}}
```

### 650 - Get player rank list
```json
{"c":650,"o":"251","p":{"start":0,"end":29}}
```

### 651 - Get alliance rank list
```json
{"c":651,"o":"254","p":{"start":0,"end":29}}
```

### 862 - Use standard recruit
```json
{"c":862,"o":"50","p":{"extractId":1,"num":1,"useDiamond":false,"isFree":true,"useHaveNum":false}}
```

### 862 - Use elite recruit
```json
{"c":862,"o":"54","p":{"extractId":2,"num":1,"useDiamond":false,"isFree":true,"useHaveNum":false}}
```

### 862 - Research skill
```json
{"c":862,"o":"57","p":{"extractId":4,"num":1,"useDiamond":false,"isFree":true,"useHaveNum":false}}
```

### 1143 - Get alliance tech list
```json
{"c":1143,"o":"99","p":{}}
```

### 1144 - Research alliance tech
```json
{"c":1144,"o":"100","p":{"scienceId":10100,"type":1}}
```

### 1149 - Get alliance store list
```json
{"c":1149,"o":"124","p":{}}
```

### 1150 - Buy from alliance store
```json
{"c":1150,"o":"126","p":{"shopId":7,"amount":1}}
```