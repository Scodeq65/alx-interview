#!/usr/bin/python3

import sys
import re
import signal


# Initialize metrics
total_size = 0
status_counts = {}
log_count = 0


# Define regular expression for log lines
log_pattern = re.compile(r'(?P<ip>\S+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d+) (?P<size>\d+)')
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

def print_metrics():
    """ Print the accumulated metrics """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    """ Handle signal interrupt """
    print_metrics()
    sys.exit(0)

# Set up signal handler for graceful termination
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            # Update total file size
            total_size += int(data['size'])
            # Update status count
            status = int(data['status'])
            if status in valid_status_codes:
                if status in status_counts:
                    status_counts[status] += 1
                else:
                    status_counts[status] = 1
            log_count += 1
            # Print metrics every 10 lines
            if log_count % 10 == 0:
                print_metrics()
        else:
            print(f"Invalid log line: {line.strip()}", file=sys.stderr)
except Exception as e:
    print(f"Error processing log: {e}", file=sys.stderr)
finally:
    print_metrics()
