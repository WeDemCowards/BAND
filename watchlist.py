from datetime import datetime, timedelta
import subprocess

class Suspect:
    def __init__(self, ip_addr: str, timestamp):
        self.ip_addr = ip_addr
        self.timestamps = [timestamp]
    
    def cull_timestamps(self, cutoff_time: datetime):
        self.timestamps = [ts for ts in self.timestamps if ts >= cutoff_time]

class Watchlist:
    def __init__(self, threshold: int, timeframe: int):
        self.suspects = []
        self.threshold = threshold # number of flags until ban
        self.timeframe = timeframe # number of seconds until flags are disregarded
    
    def add_timestamp(self, addr: str, timestamp: datetime):
        for s in self.suspects:
            if s.ip_addr == addr:
                s.timestamps.append(timestamp)
                s.cull_timestamps(datetime.now() - timedelta(seconds=self.timeframe))
                if len(s.timestamps) > self.threshold:
                    print("DEBUG --> BANNING " + s.ip_addr)
                    subprocess.call("ufw deny from " + addr)
                return
        self.suspects.append(Suspect(addr, timestamp))