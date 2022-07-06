#!/usr/bin/python3
def roman_to_int(roman_str):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(roman_str)):
        if i > 0 and roman[roman_str[i]] > roman[roman_str[i - 1]]:
            int_val += roman[roman_str[i]] - 2 * roman[roman_str[i - 1]]
        else:
            int_val += roman[roman_str[i]]
    return int_val
