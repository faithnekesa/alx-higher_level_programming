#!/usr/bin/python3
"""A function that defines a string to json function"""
import json


def to_json_string(my_obj):
    """Return json representation of a string object"""
    return json.dumps(my_obj)
