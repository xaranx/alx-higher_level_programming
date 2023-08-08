#!/usr/bin/python3
for b in range(ord('a'), ord('z') + 1):
    if b == 101 or b == 113:
        continue
    print("{:c}".format(b), end="")
