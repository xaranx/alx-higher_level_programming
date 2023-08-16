#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_str = set()
    for str in set_1:
        if str in set_2:
            common_str.add(str)
    return common_str
