#!/usr/bin/python3
"""Defining a class, Square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """__init__, initializes the size value of the square.

        Args:
            size (:obj:`int`, optional): The size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current area of square"""
        return self.__size ** 2
