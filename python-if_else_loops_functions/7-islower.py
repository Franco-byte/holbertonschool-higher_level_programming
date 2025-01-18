#!/usr/bin/python3
def islower(c):
    for _char in range(97, 123):
        if ord(c) == _char:
            return True
        else:
            return False
