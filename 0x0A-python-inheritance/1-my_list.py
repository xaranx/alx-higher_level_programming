#!/usr/bin/python3

""" Module for printed_sorted function"""


class MyList(list):
    def print_sorted(self):
        """return printed ascending sorted list"""
        print(sorted(list(self)))
