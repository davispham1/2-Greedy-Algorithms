from collections import deque

def lru(k, requests):
    cache = set()
    last_time = {}
    misses = 0

    for t, x in enumerate(requests):
        #hit
        if x in cache:
            last_time[x] = t
            continue

        misses += 1

        if len(cache) == k:
            lru = None
            lru_time = None
            for i in cache:
                used_time = last_time[i]
                if lru_time is None or used_time < lru_time:
                    lru_time = used_time
                    lru = i
            cache.remove(lru)
            last_time.pop(lru, None)

        cache.add(x)
        last_time[x] = t

    return misses
