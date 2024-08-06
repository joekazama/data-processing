import re

log_data = open(r"C:\Users\comp\PycharmProjects\parser project\tobeparsed.txt", "r").read()
print(log_data)

#Jun 16 14:15:02 2024 daemon.info crond: CMD (dhcp_lease_file) /sbin/dhcpd -t /var/lib/dhcp/dhcpd.leases
#Jun 16 14:15:03 2024 kern.warning DHCP: Lease obtained by 192.168.1.100 (00:1a:2b:3c:4d:5e) - lease time 86400 seconds

pattern = r"^(?P<date>\S+\s+\d+)\s+(?P<time>\d+:\d+:\d+)\s+(?P<year>\d+)\s+(?P<facility>\S+)\.(?P<severity>\S+)\s+(?P<message>.*)$"

# Initialize empty lists for each category
dates = []
times = []
facilities = []
severities = []
messages = []

# Parse each log line
for line in log_data.splitlines():
  match = re.match(pattern, line)
  if match:
    # Extract data from the match object
    dates.append(match.group("date"))
    times.append(match.group("time"))
    facilities.append(match.group("facility"))
    severities.append(match.group("severity"))
    messages.append(match.group("message"))
  else:
    print(f"Error parsing line: {line}")  # Handle potential invalid lines

# Print the parsed data (optional)
print("Dates:", dates)
print("Times:", times)
print("Facilities:", facilities)
print("Severities:", severities)
print("Messages:", messages)