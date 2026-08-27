#!/usr/bin/env python3
"""Defines a VerboseList class"""


class VerboseList(list):
    """A list that prints notifications when modified"""

    def append(self, item):
        """Add an item to the list and print a notification"""
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, iterable):
        """Extended the list and print a notification"""
        super().extend(iterable)
        print("Extended the list with [{}] items".format(len(iterable)))

    def remove(self, item):
        """Remove an item from the list and print a notification"""
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index=-1):
        """Remove and return an item, printing a notification"""
        item = super().pop(index)
        print("Popped [{}] from the list".format(item))
        return item
