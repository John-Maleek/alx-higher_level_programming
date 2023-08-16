#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        keys_list = list(a_dictionary)
        values_list = [a_dictionary[item] for item in keys_list]
        values_list.sort()
        best_val = values_list[-1]
        if best_val is None:
            return None
        for key, val in a_dictionary.items():
            if val == best_val:
                return key
    else:
        return None
