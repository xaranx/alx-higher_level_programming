#!/usr/bin/python3


"""This class defines a Square classe"""


class Square:
    """Square class with Private instance attr type int """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
