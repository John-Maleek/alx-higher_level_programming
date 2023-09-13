#!/usr/bin/python3
"""Module defines a class"""


class MyInt(int):
    """Inverts int operators == and !=."""
    def __ne__(self, value):
        """inverts != operator with =="""
         return self.real == value
    def __eq__(self, value):
        """inverts == operator with !="""
        return self.real != value
