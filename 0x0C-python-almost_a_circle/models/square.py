#!/usr/bin/python3
from models.rectangle import Rectangle

"""class Square that inherite from Rectangle"""


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructore """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """Str method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
