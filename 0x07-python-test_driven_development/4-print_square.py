#!/usr/bin/python3
"""Module defines a function that a square"""


def print_square(size):
    """Prints a square using the charater, #.

    Args:
        size (int): The length of a side of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
