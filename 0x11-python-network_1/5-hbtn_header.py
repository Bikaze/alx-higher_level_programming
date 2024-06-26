#!/usr/bin/python3
"""This python script takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    print(response.headers.get("X-Request-Id"))
