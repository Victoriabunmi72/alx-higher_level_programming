#!/bin/bash/python3
# Bash script that takes in a URL
curl -s "${1}" | wc -c
