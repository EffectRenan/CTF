**Challenge:** http://159.65.249.122:4118/?dom=

Payload: `<body onload=eval(name)>`.

Create an HTTP server or you can use some online solutions like https://webhook.site/ or https://requestbin.com/ to host the `index.html` file.

Edit the `index.html` file.

Access `http://159.65.249.122:4118/contact` to get the bytes for hash collision.

Use [this python script](https://gist.github.com/EffectRenan/2425aa1ab52e35f6f8ee8b31b2582d65) to generate a hash collision.
  - `python2 MD5-collision.py "<bytes given>" 0`

Send the URL to Admin and you will receive a request with the flag.

**Flag:** HACKAFLAG{1_c4nt_f0rg3t_th4t_dr34m}
