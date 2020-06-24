**Challenge:** http://159.65.249.122:3183/

*The exploit is not complete*. See the index.html file.

An error is triggered: `mixed content` between `https://tpc.googlesyndication.com` and `http://159.65.249.122:3183/`.

If you solve it, create an HTTP server hosting index.html file and send the URL at http://159.65.249.122:3183/contact.

Use [this python script](https://gist.github.com/EffectRenan/2425aa1ab52e35f6f8ee8b31b2582d65) to generate a hash collision.
  - `python2 MD5-collision.py "<bytes given>" 0`


**Flag:** ...
