#!/usr/bin/python3


"""
Module of the write function
"""


def write_file(filename="", text=""):
    """
    Methode write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
