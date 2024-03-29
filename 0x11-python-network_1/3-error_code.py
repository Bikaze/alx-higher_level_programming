#!/usr/bin/python3
""" This script takes a url and email as arguments and passes the email as
a parameter and displays the body of the response (decoded in utf-8)"""
if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv
    try:
        with urlopen(argv[1]) as response:
            data = response.read().decode("utf-8")
    except HTTPError as e:
        print("Error code: ", e.code)
    else:
        print(data)

