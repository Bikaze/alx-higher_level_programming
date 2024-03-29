#!/usr/bin/python3
"""Github commits Interview question"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    data = response.json()
    i = 0
    while i < 10 and i < len(data):
        print(f"{data[i]['sha']}: {data[i]['commit']['author']['name']}")
        i += 1
