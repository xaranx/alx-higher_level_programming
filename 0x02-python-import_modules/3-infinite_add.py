#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    leng = len(argv)
    if leng == 1:
        print("0")
    else:
        s = 0
        for i in range(1, leng):
            s += int(argv[i])
        print("{}".format(s))
