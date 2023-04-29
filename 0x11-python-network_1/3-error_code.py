#!/usr/bin/python3
"""
    Write a Python script that takes in a URL,
    Sends a request to the URL and displays the body;
    Of the response (decoded in utf-8).
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
        except error.HTTPError as er:
            print('Error code:', er.code)

