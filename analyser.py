"""
Python Security Log Analyzer

Analyzes SSH authentication logs and detects repeated
failed authentication attempts that may indicate
potential brute-force activity.
"""

import re
import sys
from collections import Counter

# Number of failures from one IP required to trigger an alert.

FAILURE_THRESHOLD = 5

def parse_log_line(line):
"""
Extract relevant information from an SSH authentication log entry.

```
Returns:
    tuple: (timestamp, event_type, username, source_ip)
    or None if the line does not match a known authentication event.
"""

failed_pattern = re.search(
    r"^(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)",
    line,
)

if failed_pattern:
    timestamp = failed_pattern.group(1)
    username = failed_pattern.group(2)
    source_ip = failed_pattern.group(3)

    return timestamp, "FAILED_LOGIN", username, source_ip

success_pattern = re.search(
    r"^(\w+\s+\d+\s+\d+:\d+:\d+).*Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)",
    line,
)

if success_pattern:
    timestamp = success_pattern.group(1)
    username = success_pattern.group(2)
    source_ip = success_pattern.group(3)

    return timestamp, "SUCCESSFUL_LOGIN", username, source_ip

return None
```

def analyze_log(filename):
"""Read the log file and analyze authentication activity."""

```
failed_attempts = []
successful_logins = []

try:
    with open(filename, "r", encoding="utf-8") as log_file:
        for line in log_file:
            event = parse_log_line(line.strip())

            if event is None:
                continue

            timestamp, event_type, username, source_ip = event

            if event_type == "FAILED_LOGIN":
                failed_attempts.append(
                    (timestamp, username, source_ip)
                )

            elif event_type == "SUCCESSFUL_LOGIN":
                successful_logins.append(
                    (timestamp, username, source_ip)
                )

except FileNotFoundError:
    print(f"[ERROR] Log file not found: {filename}")
    return

print("\n=== Python Security Log Analyzer ===\n")

print(f"Failed authentication attempts: {len(failed_attempts)}")
print(f"Successful logins: {len(successful_logins)}")

print("\n--- Failed Login Summary ---")

if not failed_attempts:
    print("No failed authentication attempts found.")
else:
    ip_counts = Counter(
        source_ip for _, _, source_ip in failed_attempts
    )

    for source_ip, count in ip_counts.items():
        print(f"{source_ip}: {count} failed attempt(s)")

        if count >= FAILURE_THRESHOLD:
            print(
                f"[ALERT] Potential brute-force activity "
                f"from {source_ip}"
            )

print("\n--- Successful Login Summary ---")

for timestamp, username, source_ip in successful_logins:
    print(
        f"{timestamp} | {username} | {source_ip}"
    )

print("\n--- Analysis Complete ---")
```

def main():
"""Program entry point."""

```
if len(sys.argv) != 2:
    print("Usage: python3 analyzer.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]
analyze_log(log_file)
```

if **name** == "**main**":
main()

