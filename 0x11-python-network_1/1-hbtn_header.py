#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the response header.
"""

import urllib.request
import sys

# Get the URL from the command-line argument
url = sys.argv[1]

# Use a 'with' statement to ensure proper resource management
with urllib.request.urlopen(url) as response:
    # Get the headers from the response
    headers = response.info()
    # Get the value of 'X-Request-Id' from the headers
    x_request_id = headers.get('X-Request-Id')

    # Display the value of 'X-Request-Id'
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in headers")
