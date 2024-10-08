from systemd import journal
import datetime
import re
from watchlist import Watchlist

def extract_ip(text: str):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    match = re.search(ip_pattern, text)
    return match.group(0) if match else None

# 15 flags within 5 minutes will result in a ban
threshold = 15
timeframe = 300

# holds IP addresses and timestamps
watchlist = Watchlist(threshold, timeframe)

# open systemd journal and start at the bottom, looking for sshd.service logs
j = journal.Reader()
j.this_boot()
j.seek_tail()
j.get_previous()
j.log_level(journal.LOG_INFO)
j.add_match(_SYSTEMD_UNIT="sshd.service")

# start processing incoming sshd logs
print("Scanning logs for anomalies (Ctrl+C to exit)")
while True:
    for entry in j:
        if entry['MESSAGE'].__contains__("Failed password"):
            ip = extract_ip(entry['MESSAGE'])
            watchlist.add_timestamp(ip, datetime.now())