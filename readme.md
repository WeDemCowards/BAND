# BAND

A program that monitors linux ssh logs and ban any IP address exhibiting suspicious behaviour.

- Scope will be limited.
    - Will be written to work with systemd and ufw.
	- No need for timed bans or complex analysis, a simple permaban after too many failed attempts will do.

Defining failed events:
- User unknown
- Failed Password

Ban threshold:
- Configurable. Default is 15 flags within 5 minutes.

## VM Testing

### 1. Users
```
root:klondike
aaron:worksucks
kenny:chelsea
lenny:nascar
```

### 2. Packages
- Install openssh-server
- Install ufw

### 3. Testing
- enable ufw, set sensible defaults if you want.
	- start from blank ufw
	- 
- Start SSH service. No need to change config.
- Launch a brute force attack with and without BAND enabled.