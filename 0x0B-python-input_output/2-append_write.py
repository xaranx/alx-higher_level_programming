#!/usr/bin/python3


"""
Module for append write
"""


def append_write(filename="", text=""):
    """
    Methode append write
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
