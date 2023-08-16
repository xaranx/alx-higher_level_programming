#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elem = set(set_1)
    for str in set_2:
        if str in common_elem:
            common_elem.add(str)
            return str
