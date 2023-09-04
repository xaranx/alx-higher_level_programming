#!/usr/bin/python3

""" Module that define a class called Rectangle """


class Rectangle:

    """class that defines a Rectangle"""

    number_of_instances = 0

    """Private instance attribute: width"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Public instance method that returns the rectangle area"""
    def area(self):
        return self.__width * self.__height

    """Public instance method that returns the rectangle perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """ Methode That return a string that representthe rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """ Method that return a string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ method that delete the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
