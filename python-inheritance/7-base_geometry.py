#!/usr/bin/python3
"""Defines the BaseGemoetry class"""


class BaseGeometry:
    """Represents the base geometry"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
