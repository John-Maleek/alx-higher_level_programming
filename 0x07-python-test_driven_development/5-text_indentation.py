#!/usr/bin/python3
"""Module defines function that indents text"""


def text_indentation(text):
    """Prints a given text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If given text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
