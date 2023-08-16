#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    return {item: a_dictionary.get(item) for item in sorted_dic}
