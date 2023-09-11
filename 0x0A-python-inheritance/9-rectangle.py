#!/usr/bin/python3

"""
module Base geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Module class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    initialize with and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        represent the Rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
