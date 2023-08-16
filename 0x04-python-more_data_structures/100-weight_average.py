#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    a = 0
    b = 0
    for x, y in my_list:
        a = a + (x * y)
        b = b + y
    return (a / b)
