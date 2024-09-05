#!/usr/bin/python3
"""a method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Returns True if data is a valid UTF-8 encoding, else return False."""
    for byte in data:
        if (byte > 255):
            return False
    return True
