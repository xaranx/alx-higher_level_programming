#!/usr/bin/python3
for c in range(122, 96, -1):
    c = c - 32 if c % 2 else c
    print("{}".format(chr(c)), end="")
