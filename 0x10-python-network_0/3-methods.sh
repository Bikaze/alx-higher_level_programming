#!/bin/bash
# This script takes is a URL, and displays all methods accepted by the server
curl -sL -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2
