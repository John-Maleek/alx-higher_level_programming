#!/usr/bin/python3
'''
    Implementing a class, Geometry
'''


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    '''
        defines a subclass of BaseGeometry
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
