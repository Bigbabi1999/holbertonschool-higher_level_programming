#!/usr/bin/python3
"""Function that returns an object represented by a JSON string"""

import json

def from_jsonstring(my_str):
    """Return Python object from JSON string"""
    return json.loada(my_str)
