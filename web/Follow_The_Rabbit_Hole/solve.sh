#!/bin/bash

base="cE4g5bWZtYCuovEgYSO1"
> aux

while true; do
    res=$(curl -s "http://167.71.246.232:8080/rabbit_hole.php?page=$base")
      if [[ $res == "end" ]]; then
          break
      else
        base=$(echo $res | cut -d ' ' -f3)
        echo $res >> aux
        echo $res
      fi
done

> output
for i in $(seq $(wc -l aux | cut -d ' ' -f1)); do 
    cat aux | grep "\[$i," >> output
done

content=""
for i in $(cat output | cut -d "'" -f2); do
    content="$content$i"
done

rm aux
echo $content | xxd -r -p > flag.png

echo "Flag: flag.png"
