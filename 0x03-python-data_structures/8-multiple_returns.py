#!/usr/bin/python3


def multiple_returns(sentence):
    str_len = len(sentence)
    first_char = sentence[0] if str_len > 0 else None
    return (str_len, first_char)
