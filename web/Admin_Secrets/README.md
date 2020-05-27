Challenge: http://admin_secrets.tjctf.org/

Create an account and login.

Create a post, access it and see the source code:
- ``<!-- Only the admin can see this -->``

**Alert:** Every single post that you create you'll have 2 seconds to click on "Report to Admin" to exploit it (or edit the timeout).

Create a HTTP server to receive admin's content. Example: ``sudo python3 http.server 80``.

Create a new post with exploit1.html. You need to edit some variables:
- yourHTTPServer, to receive admin's content.
- yourPostId, endpoint of previous post ("/post/`<something>"`)

Ps: Don't forget to click on "Report to Admin" immediately after access the post.

Your HTTP server will receive two requests, one from you and other from admin. You only need to decode the parameter in base64.

Now we figure out "/admin_flag". So we need to do a new request to "/admin_flag". Create a new post with exploit2.html. Edit:
- yourHTTPServer, to receive admin's content.

Decoding base64 content we notice that we can't read the flag. Now we need to bypass the filter. We can use HTML entity encode into iframe tag.

Edit the variable "payload" of explort3.html file with entire previous content of exploit2.html (including script tags). Open exploit3.html in some browser and copy the content of console (pess F12). We can do this same step with Burp Suite using "HTML encode".

The final paylaod will be:
  - ``<iframe srcdoc=<HTML_encoded> >``

Create a new post with the final payload and receive the flag.

Flag: tjctf{st0p_st3aling_th3_ADm1ns_fl4gs}
