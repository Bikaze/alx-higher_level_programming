#!/usr/bin/python3
""" This script takes a url and displays the body of the response
(decoded in utf-8)"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv
    try:
        req = Request(argv[1])
        with urlopen(req) as response:
            data = response.read().decode("utf-8")
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        print(data)
