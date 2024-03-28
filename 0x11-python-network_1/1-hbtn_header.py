#!/usr/bin/python3
# This python script takes in a URL, sends a request to the URL
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
