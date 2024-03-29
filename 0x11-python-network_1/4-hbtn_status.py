#!/usr/bin/python3
# This Python script fetches https://alx-intranet.hbtn.io/status
from requests import get

response = get("https://alx-intranet.hbtn.io/status").text

print("Body response:")
print("\t- type:", type(response))
print("\t- content:", response)
