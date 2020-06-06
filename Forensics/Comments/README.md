Challenge: Comments.zip

Unzipping all files we will figure out the flag.txt file which has `No flag here. :(`.

So looking at zip files comments `unzip -l *.zip`, we can see each zip file has one byte of the flag.

Execute: ./extract.sh

Flag: flag{4n6}
