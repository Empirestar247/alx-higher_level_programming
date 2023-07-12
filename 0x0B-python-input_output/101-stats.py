#!/usr/bin/python3

import sys

# Initialize variables
total_size = 0
status_counts = {}

try:
    # Read stdin line by line
    for line_number, line in enumerate(sys.stdin, 1):
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            continue

        ip_address = parts[0]
        date = parts[2][1:]
        status_code = parts[5]
        file_size = int(parts[6])

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print(f"Total file size: {total_size}")

            for code in sorted(status_counts.keys()):
                count = status_counts[code]
                print(f"{code}: {count}")

    # Print final statistics
    print(f"Total file size: {total_size}")

    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle keyboard interruption
    print("\nKeyboard interruption detected. Printing final statistics.")

    print(f"Total file size: {total_size}")

    for code in sorted(status_counts.keys()):
        count = status_counts[code]
        print(f"{code}: {count}")
