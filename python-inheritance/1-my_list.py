#!/usr/bin/python3
"""Defines a MyList class"""


class MyList(list):
    """A list with a method to print its sorted version"""


    def print_sorted(self):
        """print the list sorted in ascending order"""
        print(sorted(self))
