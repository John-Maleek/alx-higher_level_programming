#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    last_idx = len(my_list) - 1
    i = last_idx
    while i >= 0:
        print('{:d}'.format(my_list[i]))
        i -= 1
