Challenge: Comments.zip

Unzipping all files we will figure out the flag.txt which has `No flag here. :(`.

So looking at comments of zip files `unzip -l *.zip`, we can see each zip file has one byte of the flag.

Execute: ./extract.sh

Flag: flag{4n6}
