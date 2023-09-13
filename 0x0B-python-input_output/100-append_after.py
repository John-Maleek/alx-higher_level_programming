#!/usr/bin/python3
"""Module defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each
    line containing a specific string
    """
    with open(filename, mode='r', encoding='utf-8') as fd:
        text = fd.readlines()
        new_text = []

        for line in text:
            new_text.append(line)

            if search_string in line:
                new_text.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as new_file:
        for line in new_text:
            new_file.write(line)
