#!/usr/bin/python3

"""
class module that inherite from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherite from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialize an instance of the rectangle class
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
