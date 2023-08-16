#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_str = set()
    for str in set_1:
        if str not in set_2:
            diff_str.add(str)
    for str in set_2:
        if str not in set_1:
            diff_str.add(str)
    return diff_str
