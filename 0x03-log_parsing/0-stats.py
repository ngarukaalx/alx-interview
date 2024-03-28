#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics
"""


import sys
import re


# regular expresion to math the line
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] ' \
          r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

after_ten = 0
total_filesize = 0
status_codes = {
         '200': 0,
         '301': 0,
         '400': 0,
         '401': 0,
         '403': 0,
         '404': 0,
         '405': 0,
         '500': 0
         }
try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        after_ten += 1
        # if their is match process the line
        if match:
            filesize = match.group(4)
            total_filesize += int(filesize)
            status_code = match.group(3)
            if status_code in status_codes:
                status_codes[status_code] += 1
            sorted_codes = sorted(status_codes.keys())
            # after_ten += 1
            if after_ten == 10:
                after_ten = 0
                # ip_addr = match.group(1)
                # date = match.group(2)
                status_code = match.group(3)
                total_filesize = total_filesize - int(filesize)
                print("File size: {}".format(total_filesize))
                for code in sorted_codes:
                    if status_codes[code] != 0:
                        print("{}: {}".format(code, status_codes[code]))
except Exception:
    pass
finally:
    print("File size: {}".format(total_filesize))
    for code in sorted_codes:
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))
