#!/usr/bin/python3
"""A python script that takes in a URL"""

import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as vic:
            print(vic.read().decode('UTF-8'))
    except HTTPError as err:
        print("Enter code:{}".format(err.getcode()))
