#!/usr/bin/env python3
"""Defines a CountedIterator class"""


class CountedIterator:
    """Iterator that keeps track of the number of the items iterated"""

    def __init__(self, iterable):
        """Initialize the iterator and counter"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated"""
        return self.count
