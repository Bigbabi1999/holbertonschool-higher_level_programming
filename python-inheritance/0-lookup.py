#!/usr/bin/python3
"""Defines a function that lists an object's attribute and methods"""


def lookup(obj):
    """Return a list of an object's attributes and methods"""
    return list(dir(obj))
