#!/usr/bin/python3
"""Module writes to a text file"""


def write_file(filename="", text=""):
    """writes to a file
    Return number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write("{}\n".format(text))
