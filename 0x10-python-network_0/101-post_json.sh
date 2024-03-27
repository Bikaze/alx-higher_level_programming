#!/bin/bash
# Send a json file to the server through a POST option
curl -s -X POST $1 -d @$2
