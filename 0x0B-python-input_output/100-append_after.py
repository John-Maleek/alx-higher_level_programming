#!/usr/bin/python3
"""Module defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each
    line containing a specific string
    """
    with open(filename, mode='r+', encoding='utf-8') as fd:
        lines = fd.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines))
