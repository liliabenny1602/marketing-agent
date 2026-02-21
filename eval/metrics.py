import time

def track_latency(start):
    return round(time.time() - start, 3)

def performance_delta(old, new):
    return new - old