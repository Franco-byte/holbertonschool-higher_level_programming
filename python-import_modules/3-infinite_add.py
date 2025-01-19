#!/usr/bin/python3
import sys
if __name__ == "__main__":
    index = 1
    result = 0
    if len(sys.argv) == 1:
        print("0")

    if len(sys.argv) > 1:
        while index < len(sys.argv):
            result += int(sys.argv[index])
            index += 1
        print(f"{result}")
