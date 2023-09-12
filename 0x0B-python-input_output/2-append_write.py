#!/usr/bin/python3
"""
Module defines a function that
appends to a file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a file
    Returns: number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
