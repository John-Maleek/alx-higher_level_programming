#!/usr/bin/python3
"""Module defines a function"""

import json


def to_json_string(my_obj):
    """Returns a json representation of an
    object(string)
    """
    return json.dumps(my_obj)
