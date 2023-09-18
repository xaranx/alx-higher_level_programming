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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that write the json string representation of list_objs to a file
        """
        if list_objs is not None:            
            list_objs = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__+".json"
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(list_objs))
    
    @staticmethod
    def from_json_string(json_string):
        """
        static method that the return the list of the json string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

