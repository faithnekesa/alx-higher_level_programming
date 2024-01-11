#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
The letter must be sent in the variable q If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id
and name like this: [<id>] <name>
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
