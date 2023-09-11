#!/usr/bin/python3

"""
Module of is_kind_of_class function
"""


def inherits_from(obj, a_class):
    """
    Return:
    bool: True if the obj isinstance otherwise false
    """
    return isinstance(obj, a_class) and type(obj) != a_class
