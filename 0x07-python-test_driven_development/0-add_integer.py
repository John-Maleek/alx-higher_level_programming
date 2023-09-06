#!/usr/bin/python3
"""Module defines a function that adds integers"""


def add_integer(a, b=98):
    """Return the sum of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If neither of a nor b is not an integer or a float.
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int or type(b) is not float:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
