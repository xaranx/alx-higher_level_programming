#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    if leng != 0:
        print("{} arguments:".format(leng))
        for i in range(1, leng):
            print("{}: {}".format(i, sys.argv[i + 1]))
    else:
        print("{} arguments.".format(leng))
