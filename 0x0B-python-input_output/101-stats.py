#!/use/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


def print_metrics(total_size, status_counts):
    """
    Prints the metrics - total file size and lines by status code.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary containing counts of lines by status code.
    """
    print("Total file size:", total_size)
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))


def compute_metrics():
    """
    Computes the metrics from stdin input.
    """
    total_size = 0
    status_counts = {
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

    try:
        for line in sys.stdin:
            if line_count % 10 == 0 and line_count != 0:
                print_metrics(total_size, status_counts)

            try:
                split_line = [x for x in line.split(" ") if x.strip()]
                status_code = split_line[-2]
                file_size = int(split_line[-1].strip("\n"))
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except Exception:
                pass
            line_count += 1
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        raise
    print_metrics(total_size, status_counts)


if __name__ == "__main__":
    compute_metrics()
