#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys
import signal
from collections import defaultdict

# Initialize metrics
total_size = 0
status_counts = defaultdict(int)
log_count = 0
valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_metrics():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handle signal interrupt."""
    print_metrics()
    sys.exit(0)


# Set up signal handler for graceful termination
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            size = int(parts[-1])
            status = int(parts[-2])
            if status in valid_status_codes:
                total_size += size
                status_counts[status] += 1
            log_count += 1

            # Print metrics every 10 lines
            if log_count % 10 == 0:
                print_metrics()
        except ValueError:
            continue
except Exception as e:
    print(f"Error processing log: {e}", file=sys.stderr)
finally:
    print_metrics()
