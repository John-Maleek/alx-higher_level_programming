#!/usr/bin/python3
"""Module reads the content of a file"""


def read_file(filename=""):
    """prints the content of a file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
