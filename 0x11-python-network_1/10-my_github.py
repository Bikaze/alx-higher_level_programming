#!/usr/bin/python3
""" This script takes your GitHub credentials (username and password) and
uses the GitHub API to display your id """

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(response.json().get("id"))
