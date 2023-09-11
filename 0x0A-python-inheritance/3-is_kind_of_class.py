#!/usr/bin/python3

"""
Module of is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Return:
    bool: True if the obj isinstance otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
