#!/usr/bin/python3
from models.rectangle import Rectangle

"""class Square that inherite from Rectangle"""


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructore """
        super().__init__(size, size, x, y, id)
