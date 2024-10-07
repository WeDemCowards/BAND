import time
import os
from systemd import journal

if os.geteuid() != 0:
    print("delete comment below \n")
    #exit("User must be root. Exiting")

j = journal.Reader()
j.this_boot()
j.seek_tail()
j.get_previous()


j.log_level(journal.LOG_INFO)
j.add_match(_SYSTEMD_UNIT="sshd.service") # sshd.service? unit or t? follow up.

print("Scanning logs for anomalies (Ctrl+C to exit)")
while True:
    for entry in j:
        print(entry['MESSAGE'])
