#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width (self):
        """Retrieve the width"""
        return self.__width
