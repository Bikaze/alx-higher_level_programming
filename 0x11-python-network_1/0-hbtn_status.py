#!/usr/bin/python3
# This Python script fetches https://alx-intranet.hbtn.io/status
from urllib.request import Request, urlopen

req = Request("https://alx-intranet.hbtn.io/status")

with urlopen(req) as response:
    data = response.read()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode("utf-8"))
