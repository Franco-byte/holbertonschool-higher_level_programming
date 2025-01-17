#!/usr/bin/python3
for abc in range(97, 123):
    if abc == 101 or abc == 113:
        continue
    print("{}".format(chr(abc)), end='')
