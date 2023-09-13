#!/usr/bin/python3
"""Module defines a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle class"""
    def __init__(self, width, height):
        """initialises rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints a string representation"""
         return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
