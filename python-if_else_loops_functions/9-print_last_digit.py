#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        last_dig = number % 10
        print(f"{last_dig}", end='')
        return last_dig
    else:
        last_dig = number % 10
        print(f"{last_dig}", end='')
        return last_dig
