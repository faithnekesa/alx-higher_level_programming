#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id. You must use Basic Authentication
with a personal access token as password to access to your information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
