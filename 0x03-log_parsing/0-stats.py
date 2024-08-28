#!/usr/bin/python3
import sys
import re

count = 0
cap = 10
total_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_codes_dict = {}
for line in sys.stdin:
    count += 1
