#!/usr/bin/python3


""" Module for LokedClass"""


class LockedClass:

    """
    __slots__ :attr restricts theinstance attr
    only those list as in this case "first_name"

    __slots__ = ["first_name"]
    """

    def __init__(self, first_name=""):
        self.first_name = first_name
