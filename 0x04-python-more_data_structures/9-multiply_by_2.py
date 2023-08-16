#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary)
    return {item: (a_dictionary[item] * 2) for item in key_list}
