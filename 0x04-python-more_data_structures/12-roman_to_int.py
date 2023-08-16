#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    str_list = list(roman_string)
    num_list = [roman_dict.get(str) for str in str_list]
    list_len = len(num_list) - 1
    arr = []
    sum = 0
    i = 0
    while i <= list_len:
        if list_len == 0:
            arr.append(num_list[0])
        elif i == list_len:
            arr.append(num_list[i])
        elif num_list[i] > num_list[i + 1] or num_list[i] == num_list[i + 1]:
            arr.append(num_list[i])
        else:
            arr.append(-num_list[i])
        i += 1
    for num in arr:
        sum = sum + num
    return sum
