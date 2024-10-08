# BAND

A program that monitors linux ssh logs and ban any IP address exhibiting suspicious behaviour.

- Scope will be limited.
    - Will be written to work with systemd and ufw.
	- No need for timed bans or complex analysis, a simple permaban after too many failed attempts will do.


## VM Testing
*Testing in Debian*

1. Add users with crackable passwords

2. Install necessary packages
	- openssh-server
	- ufw
	
3. Configure ufw and enable
	- start from blank ufw
	- `ufw default deny incoming`
	- `ufw allow ssh` *this needs to be written exactly so, since BAND is janky and needs to be able to delete this* (lol)

4. Start SSHD and attempt a brute force attack