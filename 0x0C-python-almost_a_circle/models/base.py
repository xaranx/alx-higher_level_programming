#!/usr/bin/python3

import os
import json
import csv
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
        class method that write the json string
        representation of list_objs to a file
        """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        file_name = cls.__name__+".json"
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        static method that the return the list
        of the json string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns the instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method that return a list of instances
        """
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []

        with open(file_name, "r") as file:
            json_string = file.read()

        data = cls.from_json_string(json_string)
        instances = [cls.create(**item) for item in data]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write CSV string representation of list_objs to a file
        args:
            list_objs (list): list of instances that inherit from Base
        """

        filename = cls.__name__ + ".csv"

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        else:
            list_objs = []

        with open(filename, "w") as file:
            if list_objs is not None:
                fieldnames = []
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        return a list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                list_dicts = csv.DictReader(file)
                list_dicts = [dict([key, int(value)]
                                   for key, value in dictionary.items())
                              for dictionary in list_dicts]
            return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
