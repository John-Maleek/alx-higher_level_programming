#!/usr/bin/python3
"""Defining a class, Square"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """__init__

        __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
