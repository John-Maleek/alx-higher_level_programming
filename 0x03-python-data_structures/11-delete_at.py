#!/usr/biin/python3


def delete_at(my_list=[], idx=0):
    last_idx = len(my_list) - 1
    new_list = []
    if idx > last_idx or idx < 0:
        return my_list
    else:
        for el in my_list:
            if el == my_list[idx]:
                continue
            else:
                new_list.append(el)
        return new_list
