#!/usr/bin/python3
"""
    Module defines a class
"""


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """initialises Rectangle class"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
