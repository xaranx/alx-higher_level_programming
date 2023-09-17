#!/usr/bin/python3

import json
"""
Module base
"""


class Base():
    """
    private class attr
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static methode returns the JSON string representaton of list_dict
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
