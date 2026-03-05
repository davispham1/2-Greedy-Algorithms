"""FIFO"""
from collections import deque

def fifo(k, requests):
    cache = set()
    q = deque()
    misses = 0

    for x in requests:
        if x in cache:
            continue

        misses += 1

        if len(cache) == k:
            #fifo 
            evict = q.popleft()
            cache.remove(evict)

        cache.add(x)
        q.append(x)

    return misses
