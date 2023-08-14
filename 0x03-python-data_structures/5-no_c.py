#!/usr/bin/python3


def no_c(my_string):
    c = 'c'
    C = 'C'
    new_str_list = []
    for char in my_string:
        if char == c:
            continue
        elif char == C:
            continue
        else:
            new_str_list.append(char)
    new_str = ''.join([char for char in new_str_list])
    return new_str
