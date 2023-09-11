#!/usr/bin/python3

""" Module for printed_sorted function"""


class MyList(list):
    """class inherit from list"""

    def print_sorted(self):
        """print the list in ascending order"""
        print(sorted(list(self)))
