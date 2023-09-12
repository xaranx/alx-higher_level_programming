#!/usr/bin/python3

"""
Module for read file methode
"""


def read_file(filename=""):
    """
    Methode for Read line
    """
    with open("filename", encoding="utf-8") as f:
        print(f.read(), end="")
