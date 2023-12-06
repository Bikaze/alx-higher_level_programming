#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    s = list(roman_string)
    number = 0
    i = 0
    while i < len(s):
        if i != len(s) - 1 and num[s[i]] < num[s[i+1]]:
            number += num[s[i+1]] - num[s[i]]
            i += 2
        else:
            number += num[s[i]]
            i += 1
    return number
