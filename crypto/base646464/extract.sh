#!/usr/bin/env sh

decoded=$(cat cipher.txt)
while [[ true ]]; do
  {
    tmp=$decoded
    decoded=$(echo $decoded | base64 -d 2>&1)
  } || {
    echo $tmp
    exit
  }
done
