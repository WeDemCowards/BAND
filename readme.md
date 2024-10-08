# BAND

A program that monitors linux ssh logs and ban any IP address exhibiting suspicious behaviour.

- Scope will be limited.
    - Will be configured to work with ufw.
	- No need for timed bans or complex analysis, a simple permaban after too many failed attempts will do.

Defining failed events:
- User unknown
- Failed Password

Ban threshold:
- "Too many" failed attempts in a short amount of time.
- This will be hardcoded and not configurable.

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
- Start SSH service. No need to change config.
- Launch a brute force attack with and without BAND enabled.