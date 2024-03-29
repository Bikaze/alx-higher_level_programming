#!/usr/bin/python3
"""This script takes a url and email as arguments and passes the email as
a parameter and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    parameters = {'email': argv[2]}

    response = get(argv[1], params=parameters)
    print(response.text)
