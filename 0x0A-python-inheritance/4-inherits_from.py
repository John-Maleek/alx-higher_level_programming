#!/usr/bin/python3
"""Module defines a function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited directly or indirectly) from the specified class;
    otherwise False
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
