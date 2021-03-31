
<html>
<title>
$Echo
</title>
<h1>$Echo</h1>
<body>
<form method="get" name="index.php">
<input type="text" name="echo" id="echo" size="80">
<input type="submit" value="Echo">
</form>
<h3>
<html> <title> $Echo </title> <h1>$Echo</h1> <body> <form method="get" name="<?php echo basename($_SERVER['PHP_SELF']); ?>"> <input type="text" name="echo" id="echo" size="80"> <input type="submit" value="Echo"> </form> <h3> <?php $to_echo = $_REQUEST['echo']; $cmd = "bash -c 'echo " . $to_echo . "'"; if(isset($to_echo)) { if($to_echo=="") { print "Please don't be lame, I can't just say nothing."; } elseif (preg_match('/[#!@%^&*()$_+=\-\[\]\';,{}|":>?~\\\\]/', $to_echo)) { print "Hey mate, you seem to be using some characters that makes me wanna throw it back in your face >:("; } elseif ($to_echo=="cat") { print "Meowwww... Well you asked for a cat didn't you? That's the best impression you're gonna get :/"; } elseif (strlen($to_echo) > 15) { print "Man that's a mouthful to echo, what even?"; } else { system($cmd); } } else { print "Alright, what would you have me say?"; } ?> </h3> <div style="position:fixed; bottom:1%; left:1%;"> <br><br><br><br> <b> NOT CHALLENGE RELATED:</b><br>THANK YOU to HackerOne for supporting NahamCon and NahamCon CTF! <p> <img width=600px src="https://www.fstech.co.uk/fst/hacker-powered-security-report/logo.png"> </p> </div> </body> <script>document.getElementById("echo").focus();</script> </html>
</h3>

<div style="position:fixed; bottom:1%; left:1%;">
<br><br><br><br>
<b> NOT CHALLENGE RELATED:</b><br>THANK YOU to HackerOne for supporting NahamCon and NahamCon CTF!
<p>
<img width=600px src="https://www.fstech.co.uk/fst/hacker-powered-security-report/logo.png">
</p>
</div>


</body>
<script>document.getElementById("echo").focus();</script>

</html>
