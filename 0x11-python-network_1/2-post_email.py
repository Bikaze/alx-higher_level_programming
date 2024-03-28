#!/usr/bin/python3
# This script takes a url and email as arguments and passes the email as
# a parameter
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    args = urllib.parse.urlencode({'email': argv[2]})
    args = args.encode('utf-8')
    req = urllib.request.Request(argv[1], args)
    with urllib.request.urlopen(req) as response:
        print(reponse.read().decode("utf-8"))
