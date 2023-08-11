#!/usr/bin/python3
import sys

def add_args(argv):
    args = len(argv) - 1
    if args == 0:
        print("{:d}".format(args))
        return
    else:
        count = 1
        total = 0

        while count <= args:
            total = total + int(argv[count])
            count += 1

        print("{:d}".format(total))

if __name__ == "__main__":
    add_args(sys.argv)
