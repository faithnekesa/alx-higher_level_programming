#!/usr/bin/python3
"""A file-reading function definition"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
