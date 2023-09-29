#!/usr/bin/python3
"""
Module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with a letter as a parameter
"""
import requests
import sys
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        id_ = r.json()['id']
        name_ = r.json()['name']
        print("[{}] {}".format(id_, name_))
    except ValueError:
        print("Not a Valid Json")
    except KeyError:
        print("No result")
