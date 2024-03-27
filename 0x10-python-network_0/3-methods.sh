#!/bin/bash
# This script takes is a URL, and displays all methods accepted by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
