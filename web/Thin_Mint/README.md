**Challenge***: https://thinmint-baeaa80f.challenges.bsidessf.net

We need to edit the cookies to get the flag.

294de3557d9d00b3d2d8a1e6aab028cf (md5) = anynymous
21232f297a57a5a743894a0e4a801fc3 (md5) = admin

The `tm_admin` must to be 1 and `tm_user` must be the string `admin` encoded in MD5.

=> Cookie: tm_admin=1; tm_user=21232f297a57a5a743894a0e4a801fc3

**Flag**: CTF{iAmAdm1n} 

