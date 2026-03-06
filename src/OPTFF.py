from collections import deque

def optff(k, requests):
    future = {}
    for i, x in enumerate(requests):
        if x not in future:
            future[x] = deque()
        future[x].append(i)

    cache = set()
    misses = 0
    never = len(requests) + 1

    for i, x in enumerate(requests):
        future[x].popleft()

        if x in cache:
            continue

        misses += 1

        if len(cache) == k:
            evict = None
            farthest = -1

            for r in cache:
                if len(future[r]) > 0:
                    next = future[r][0]
                else:
                    next = never

                if next > farthest:
                    farthest = next
                    evict = r

            cache.remove(evict)

        cache.add(x)

    return misses