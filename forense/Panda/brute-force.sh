#!/usr/bin/env sh

for (( i = 0; i < 10; i++ )); do
  for (( j = 0; j < 10; j++ )); do
    for (( k = 0; k < 10; k++ )); do
      for (( l = 0; l < 10; l++ )); do
          unzip -o -qq -P $i$j$k$l panda.zip 2>/dev/null
          if [[ $? == 0 ]]; then
            echo "Password: $i$j$k$l"
            exit
          fi
      done
    done
  done
done
