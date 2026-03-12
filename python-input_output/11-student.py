#!/usr/bin/python3
"""Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation"""
        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__


    def reload_from_json(self, json):
        """Replace attributes from dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
