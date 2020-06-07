Challenge: https://debt-simulator.web.hsctf.com/

You need to read code of `main.1b8f0187.chunk.js`.

The app is doing an HTTP Post request to `https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001` with parameters `function=getPay/getCost` when we click on button `Play again`

So we can make an HTTP Get request to `https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001`. The content of response will be `{"functions":["getPay","getCost","getgetgetgetgetgetgetgetgetFlag"]}`

It means we can make an HTTP Post request to `https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001` with parameter `function=getgetgetgetgetgetgetgetgetFlag` and get the flag.

Flag: flag{y0u_f0uND_m3333333_123123123555554322221}
