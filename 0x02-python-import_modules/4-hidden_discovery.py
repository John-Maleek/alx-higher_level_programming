#!/usr/bin/python3


def print_names(hidden_4):
    hidden_names = dir(hidden_4)
    for name in hidden_names:
        if name.startswith('__'):
            continue
        else:
            print("{:s}".format(i))


if __name__ == "__main__":
    import hidden_4
    print_names(hidden_4)
