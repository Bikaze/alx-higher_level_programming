#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    arg = ""
    if len(argv) > 1:
        arg = argv[1]
    parameters = {'q': arg}

    response = post("http://0.0.0.0:5000/search_user", data=parameters)
    if response.json() == {}:
        print("No result")
    elif not response.json():
        print("Not a valid JSON")
    else:
        r = response.json()
        print(f"[{r.get('id')}] {r.get('name')}")
