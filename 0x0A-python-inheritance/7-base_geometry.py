#!/usr/bin/python3
"""Module defines a class"""


class BaseGeometry:
    """creates a simple class"""
    def area(self):
        """not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates the given 'value'"""
        if type(value) is not int:
            raise Exception('{} must be an integer'.format(name))
        if value <= 0:
            raise Exception('{} must be greater than 0'.format(name))
