#!/usr/bin/python3
"""Module defines a script that hat adds all arguments
to a Python list, and then save them to a file
"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        result = load_from_json_file("add_item.json")
    except FileNotFoundError:
        result = []
    for i in range(1, len(sys.argv)):
        result.append(sys.argv[i])
    save_to_json_file(result, "add_item.json")
