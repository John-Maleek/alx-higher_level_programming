#!/usr/bin/python3
"""Module defines a class"""


class MyList(list):
    """Defines a class"""
    def print_sorted(self):
        """Retruns a sorted list"""
        return sorted(self)
