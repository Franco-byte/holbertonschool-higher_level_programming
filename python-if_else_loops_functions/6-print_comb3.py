#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(1, 10):
        if num2 <= num1:
            continue
        if num1 == 8 and num2 == 9:
            break
        print("{}{}".format(num1, num2), end= ', ')
print(89)
