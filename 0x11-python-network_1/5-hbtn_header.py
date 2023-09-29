#!/usr/bin/python3
"""
A script that sends a GET request to a specified URL and displays the value
of the X-Request-Id header variable found in the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
