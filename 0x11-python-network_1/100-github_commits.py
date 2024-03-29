#!/usr/bin/python3
"""Github commits Interview question"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    data = response.json()
    for i in range(10):
        print(f"{data[i]['sha']}: {data[i]['commit']['author']['name']}")
