#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    last_idx = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > last_idx:
        return my_list
    else:
        my_list[idx] = element
        return my_list
