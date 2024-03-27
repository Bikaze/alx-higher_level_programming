#!/bin/bash
# This script takes in a host, and submits a GET request with a header
curl -sH "X-school-User-Id: 98" "$1"
