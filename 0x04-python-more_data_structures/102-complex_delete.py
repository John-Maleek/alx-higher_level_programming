#!/usr/bin/python3
def complex_delete(my_dict, value):
    arr = []
    for key, val in my_dict.items():
        if val is value:
            arr.append(key)
    for item in arr:
        del my_dict[item]
    return my_dict
