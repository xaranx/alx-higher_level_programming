#!/usr/bin/python3
for c in range(25, -1, -1):
    if c % 2 == 0:
        print(chr(65 + c), end="")
    else:
        print(chr(97 + c), end="")

