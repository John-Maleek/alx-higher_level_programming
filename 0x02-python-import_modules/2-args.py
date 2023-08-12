#!/usr/bin/python3


def print_arg(argv):
    args = len(argv) - 1
    if args == 0:
        print("{:d} arguments:".format(args))
        return
    else:
        if args == 1:
            print("{:d} argument:".format(args))
        else:
            print("{:d} arguments:".format(args))
        count = 1
        while count <= args:
            print("{:d}: {:s}".format(count, argv[count]))
            count += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
