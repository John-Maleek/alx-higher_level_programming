#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    last_idx = len(my_list) - 1
    if idx < 0:
        return list_copy
    elif idx > last_idx:
        return list_copy
    else:
        list_copy[idx] = element
        return list_copy