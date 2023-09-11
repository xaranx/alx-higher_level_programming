#!/usr/bin/python3

"""
Module for lookup function
"""


def lookup(obj):
    """Return the list of available attr and methode of obj"""
    return dir(obj)
