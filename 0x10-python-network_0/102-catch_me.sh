#!/bin/bash
# This script makes a request and causes the server to respond by "You got me!"
curl -sw "You got me!" -o /dev/null 0.0.0.0:5000/catch_me
