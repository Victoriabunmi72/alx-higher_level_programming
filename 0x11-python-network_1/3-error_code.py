#!/usr/bin/python3
"""A python script that takes in a URL"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as d:
            print(d.read().decode('utf-8'))
    except HTTPError as err:
        print("Enter code:{}".format(err.getcode()))
