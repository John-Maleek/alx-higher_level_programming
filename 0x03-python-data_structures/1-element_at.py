#!/usr/bin/python3


def element_at(my_list, idx):
    last_idx = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > last_idx:
        return None
    else:
        return my_list[idx]
