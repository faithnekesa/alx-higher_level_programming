#!/usr/bin/python3
"""A function that defines a JSON to obect function"""
import json


def from_json_string(my_str):
    """Return python representation of a json object"""
    return json.loads(my_str)
