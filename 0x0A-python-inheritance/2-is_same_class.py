#!/usr/bin/python3

""" Module issaneclass function"""


def is_same_class(obj, a_class):
    """
    Return:
    bool: true if the obj is instance of a_class
    """
    return type(obj) == a_class
