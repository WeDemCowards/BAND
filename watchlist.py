import datetime

class Suspect:
    def __init__(self, ip_addr: str):
        self.ip_addr = ip_addr
        self.timestamps = []
    
    def cull_timestamps(self, cutoff_time: datetime):
        self.timestamps = [ts for ts in self.timestamps if ts >= cutoff_time]

class Watchlist:
    def __init__(threshold: int, timeframe: int):
        self.suspects = []
        self.threshold = threshold # number of flags until ban
        self.timeframe = timeframe # number of seconds until flags are disregarded
    
    def add_timestamp(addr: str, timestamp: datetime):
        found = False
        for s in self.suspects:
            if s.ip_addr = addr:
                found = True
                s.timestamps.append(timestamp)
                s.cull_timestamps(datetime.now() - timedelta(seconds=timeframe))
    
    