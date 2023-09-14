#!/usr/bin/python3
"""
    Module defines a class Square
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
        Defines a subclass of rectangle
    """
    def __init__(self, size):
        """initialises square"""
        self.integer_validator('size', size)

        self.__size = size
        super().__init__(self.__size, self.__size)
