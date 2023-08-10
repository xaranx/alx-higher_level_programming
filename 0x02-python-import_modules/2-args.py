#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    if leng == 1:
        print("{} argument:".format(leng))
        print("{}: {}".format(leng, sys.argv[1]))
    elif leng  == 0:
        print("{} arguments.".format(leng))
    else:
        print("{} arguments:".format(leng))
        for i in range(0, leng):
            print("{}: {}".format(i, sys.argv[i + 1]))    
