#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    rom_list = list(roman_string)
    integer = 0

    for i in range(len(rom_list)):
        if i + 1 < len(rom_list) and roman[rom_list[i]] < roman[rom_list[i + 1]]:
            integer -= roman[rom_list[i]]
        else:
            integer += roman[rom_list[i]]
    return integer
