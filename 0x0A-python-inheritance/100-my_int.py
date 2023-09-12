#!/usr/bin/python3

"""
class module Myint
"""


class MyInt(int):
    """
    MyInt class that inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides equality operator.
        """

        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides inequality operator.
        """

        return super().__eq__(other)
