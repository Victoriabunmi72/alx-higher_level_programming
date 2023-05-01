#!/usr/bin/python3
"""A python script that takes in a URL"""

if __name__ == "__main__":

    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
        except urllib.error.HTTPError as er:
            print('Enter code:', er.code)
