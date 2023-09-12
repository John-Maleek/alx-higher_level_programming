#!/usr/bin/python3
"""Module defines a function that returns
returns an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """returns and object respresented by a JSON string"""
    return json.loads(my_str)
