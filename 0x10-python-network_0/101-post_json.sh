#!/bin/bash
# Send a json file to the server through a POST option
curl -sL -X POST $1 -H "Content-Type: application/json" -d @$2
