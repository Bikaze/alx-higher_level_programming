#!/usr/bin/python3
# This python script takes in a URL, sends a request to the URL
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
