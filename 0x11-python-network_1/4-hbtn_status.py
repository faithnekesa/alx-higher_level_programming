#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests"""

import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
