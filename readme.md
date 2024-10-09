# BAND

A program that monitors linux ssh logs and ban any IP address exhibiting suspicious behaviour.

- Scope will be limited.
    - Will be written to work with systemd and ufw.
	- No need for timed bans or complex analysis, a simple permaban after too many failed attempts will do.

# Testing Brute force attacks

You should have two virtual machines, an attacker(kali) and a victim. (victim is preferably debian or debian based)
If you are attempting to make this work on a machine that is not debian, you may run into problems. Message me if you need a hand!

### Configure machines on NAT Network
For the machines to be able to interact, they have to be on the same virtual network.

In Virtualbox, set up a NAT network:
- Navigate to tools > NAT Networks and use the Create button.
- In each machine's settings, set "Attached to:" to NAT Network, and make sure the Name is correct.

### Victim

- Add users to victim machine with `adduser` and `passwd`.
    - Passwords should be weak, check a common password list.
- install necessary packages
    - openssh-server
    - ufw
    - python3-systemd
- open ssh server with `sudo systemctl enable sshd`
- configure ufw
    - `sudo ufw default deny incoming`
    - `sudo ufw allow ssh`
    - `sudo ufw enable`
- At this point you can decide if you want to test a brute force with or without the tool.
    - If you are using the tool, `sudo python3 band.py` will monitor logs for you.
    - If not, you can still monitor logs with `sudo journalctl -t sshd -f`

### Attacker

- Prepare a password list. You can find plenty at /usr/share/wordlists on kali.
- To launch a brute force attack use the following command
    - `hydra -l <login> -P <password_list.txt> -t 6 ssh://<VICTIM_IP_ADDRESS>`
- This could take a long time depending on the strength of the victim's password.
