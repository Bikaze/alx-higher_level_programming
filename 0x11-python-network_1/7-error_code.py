#!/usr/bin/python3
"""This script takes a url and displays the body of the response
(decoded in utf-8)"""

if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        response = requests.get(argv[1])
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error code:", response.status_code)
    else:
        print(response.text)
