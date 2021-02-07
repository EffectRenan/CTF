**Challenge:** https://web-utils.dicec.tf/ | https://us-east1-dicegang.cloudfunctions.net/ctf-2021-admin-bot?challenge=web-utils

**Source code**: https://dicegang.storage.googleapis.com/uploads/d657a11ef0f129e9339a41edb9255903e74875180e9f8ced1649bf6616b5e3d1/app.zip

We can define the type as a `link` and then use `javascript:` to exploit an XSS.

Request content:
```
{"data":"javascript:<payload>","type":"link"}

```

We can use `eval-charcode.js` to generate an encoded payload.

**Flag**: dice{f1r5t_u53ful_j4v45cr1pt_r3d1r3ct}
