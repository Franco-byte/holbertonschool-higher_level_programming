#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numargs = len(sys.argv)
    count = 1
    index = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    if len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if len(sys.argv) > 3:
        print("{} arguments:".format(numargs - 1))
        while index < len(sys.argv):
            print("{}: {}".format(count, sys.argv[index]))
            count += 1
            index += 1
