#!/usr/bin/python3
import sys
"""Checks if argument is a number >= 4"""


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit()

try:
    num = int(sys.argv[1])
    if num < 4:
        print("N must be at least 4")

except ValueError:
    print("N must be a number")
