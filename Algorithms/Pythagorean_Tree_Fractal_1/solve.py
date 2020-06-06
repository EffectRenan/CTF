#!/usr/bin/env python

import sys

# (2 ** (n-1)) + (2 ** (n-2)) + ... + (2 ** 0) = (2 ** n) - 1

result = 0
for i in range(int(sys.argv[1])):
    result += 2 ** i

print("flag{%s}" %result)
