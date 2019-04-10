#!/usr/bin/env python3

import sys

args = sys.argv[1:]
top = args[0] if args else 100
for i in range(1, int(top) + 1):
    if i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')

print()
