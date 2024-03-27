#!/bin/bash
# This script takes is a URL, sends a GET request to print only the status code
curl -sw "%{http_code}" -o /dev/null "$1"
