#!/bin/bash
# This script takes is a URL, sends an OPTION request to the input host
curl -sLX OPTIONS "$1"
