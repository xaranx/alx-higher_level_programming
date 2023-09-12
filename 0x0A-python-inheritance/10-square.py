#!/usr/bin/python3

"""
class Module of rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    initialize with size
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        
        self.__size = size
    def area(self):
        """
        calculate the area
        """
        return self.__size * self.__size
    
    def __str__(self):
        """
        representation of square
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
