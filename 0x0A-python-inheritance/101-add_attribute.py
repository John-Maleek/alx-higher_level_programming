#!/usr/bin/python3
"""Module defines a class"""


def add_attribute(obj, attr, value):
    """adds new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
