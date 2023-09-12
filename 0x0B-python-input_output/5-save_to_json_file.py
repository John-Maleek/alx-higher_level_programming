#!/usr/bin/python3
"""Module defines a function that writes an Object
to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        data = json.dumps(my_obj)
        return fd.write(data)
