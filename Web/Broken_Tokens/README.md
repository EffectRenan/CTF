Challenge: https://broken-tokens.web.hsctf.com/

The main page shows a `publickey.pem` file which we can use it to generate a new JWT token.

Every single credentials which we try to login, we will be redirect to `guest` user.

We can copy the cookie (JWT token) and see what means. Use this site `https://jwt.io/`

Now we sow the fields `"alg": "RS256"` and `"auth": "guest"`. We can change it to `"auth": "admin"` and generate a new valid token.

Execute: python exploit.py

Flag: flag{1n53cur3_tok3n5_5474212}
