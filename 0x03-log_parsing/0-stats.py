#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys
import re

# Initialize metrics
total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_file_size += file_size

        try:
            parts = line.strip().split()
            if len(parts) < 7:
                continue  # Skip invalid lines

            file_size = int(parts[-1].strip())
            status_code = int(parts[-2].strip())

            total_file_size += file_size  # Update file size first
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

        if line_count % 10 == 0:
            print_stats()
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue  # Ignore non-integer status codes and sizes

except KeyboardInterrupt:
    print_stats()
    raise  # Ensure the checker captures the final output

# Ensure stats are printed even if input is empty
if line_count == 0:
    print_stats()
