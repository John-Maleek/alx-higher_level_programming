#!/usr/bin/python3
"""Module defines a class"""


class Student:
    """defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict"""
        return self.__dict__
