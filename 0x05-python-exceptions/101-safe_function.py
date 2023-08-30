#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
