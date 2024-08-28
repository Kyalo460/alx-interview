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

    # Checks if input matches a pattern and parses it
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s-\s\[(.*?)\]\s"(.*?)"\s(\d+)\s(\d+)'

    match = re.match(pattern, line)

    if match is None:
        continue

    status_code = match.group(4)
    file_size = match.group(5)

    total_size += int(file_size)

    # Checks if status code is in the list of status codes
    if int(status_code) in status_codes:
        if status_code in status_codes_dict:
            status_codes_dict[status_code] += 1
        else:
            status_codes_dict[status_code] = 1

    if count == cap:
        cap += 10
        print("File size:", total_size)

        for key, value in status_codes_dict.items():
            print(f"{key}: {value}")
