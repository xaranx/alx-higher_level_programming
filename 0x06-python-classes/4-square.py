#!/usr/bin/python


"""Module define square class"""


class Square:

    """private instance attr type int"""

    def __init__(self, size=0):
        self.__size = size

    """retrieve private attr"""

    @property
    def size(self):
        return self.__size

    """set value to private attr"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
