#!/usr/bin/python3
"""Module defines a function that prints the status of
a request
"""


import sys


if __name__ == "__main__":
    counter = 0
    size = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        line = l.split()
        try:
            size += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except:
            continue
        if counter == 9:
            print("File size: {}".format(size))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            counter = 0
        counter += 1
    if counter < 9:
        print("File size: {}".format(size))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))
