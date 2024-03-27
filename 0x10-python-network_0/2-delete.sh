#!/bin/bash
# This script takes is a URL, sends a DELETE request to the input host
curl -sLX DELETE "$1"
