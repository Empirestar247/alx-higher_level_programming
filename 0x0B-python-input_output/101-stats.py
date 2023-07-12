#!/usr/bin/python3

import sys
import signal

# Initialize variables
total_size = 0
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

line_count = 0


def print_statistics():
    # Print total file size
    print(f"File size: {total_size}")

    # Print number of lines by status code in ascending order
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print(f"{code}: {count}")


# Handle keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Process input lines
try:
    for line in sys.stdin:
        line_count += 1

        # Parse line
        parts = line.strip().split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
