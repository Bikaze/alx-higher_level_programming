#!/bin/bash
# This script takes is a URL, and displays all methods accepted by the server
curl -sH "X-school-User-Id: 98" "$1"
