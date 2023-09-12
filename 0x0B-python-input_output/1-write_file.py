#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        return file.write("{}\n".format(text))
