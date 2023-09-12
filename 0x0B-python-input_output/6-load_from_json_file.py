#!/usr/bin/python3
"""Module defines a function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding+"utf-8") as fd:
        return json.load(fd)
