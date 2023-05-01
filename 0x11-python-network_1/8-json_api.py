#!/usr/bin/python3
"""
    Python script that takes in a letter and;
    Sends a POST request to http://0.0.0.0:5000/search_user;
    with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    data = requests.post(url, data={'q': q})
    try:
        res = data.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}"
                    .format(res['id'],
                        res['name']))
    except Exception:
        print("Not a valid JSON")
