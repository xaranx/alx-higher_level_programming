#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    status = res.status_code
    print(res.text) if status < 400 else print(
        "Error code: {}".format(res.status_code))
