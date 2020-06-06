#!/usr/bin/env sh

count=1

flag=$(unzip -o -l Comments.zip | cut -d ' ' -f2 | grep .)
unzip Comments.zip

while [[ true ]]; do
  flag+=$(unzip -o -l $count.zip | cut -d ' ' -f2 | grep .)
  {
    unzip "$count.zip"
  } || {
    break
  }
  count=$(expr $count + 1)
done

#Delete extracted files
for i in $(ls *.zip | grep -v 'C');do rm $i; done && rm flag.txt
clear; echo $flag

