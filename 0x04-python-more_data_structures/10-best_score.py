#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        keys_list = list(a_dictionary)
        values_list = [a_dictionary[item] for item in keys_list]
        values_list.sort()
        return values_list[-1]
    else:
        return None
