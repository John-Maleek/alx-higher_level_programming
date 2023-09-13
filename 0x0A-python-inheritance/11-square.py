#!/usr/bin/python3
"""Module defines a class"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Defines a square class"""
    def __init__(self, size):
        """initialises Square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """retruns string representation"""
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
