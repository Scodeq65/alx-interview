#!/usr/bin/python3
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
    """Print the metrics."""
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

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

        if line_count % 10 == 0:
            print_stats()


except KeyboardInterrupt:
    print_stats()
    raise

# Print final stats if EOF is reached
print_stats()
