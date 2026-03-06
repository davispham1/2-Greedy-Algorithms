# 2: Greedy Algorithms

Davis Pham 38499319

to compile/build and run:

```
or any py
- to run example
python3 src/main.py < example/example.in

python3 src/main.py < tests/data1.in

- run 3 files for question 1
python3 src/main.py < tests/file1.in
python3 src/main.py < tests/file2.in
python3 src/main.py < tests/file3.in

- run data2 for question 2
python3 src/main.py < tests/data2.in
```
Assumptions:
input format is:

k m
r1 r2 r3 ... rm

Where:
( k ) = cache capacity ( ( k >= 1 ) )

( m ) = number of requests

( r_1, .., r_m ) = sequence of integer IDs

no other library/dependencies needed

Written component

Question 1) Empirical Conclusion

File	k	m  FIFO LRU OPTFF
File1	3	60	48	42	30
File2	4	62	40	38	22
File3	5	55	33	33	21

a) OPTFF does have the fewest misses across all three input file

b) FIFO varies and usually does either worse or similar with LRU. For example in file1 and file2 
it did worse but file 3 it tied.

Question 2) Bad sequence

For k = 3, run data2.in

LRU misses = 10
OPTFF misses = 7

This is because LRU is based on what happened in the past, so it may end up 
keeping something that was used recently even if it will not be needed 
again for a while, and evicting something that is about to be requested soon. 
OPTFF gets to look ahead at the requests so when the cache is full it removes the item whose 
next request is farthest away (never occurs). Which allows OPTFF to
avoid misses that LRU cannot avoid.

Question 3) OPTFF is optimal
OPTFF: Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).

for the first different eviction of optff and (A). such as evicting X for optff and Y for A.
Since OPTFF chose X, Y must come back sooner than X does. keeping the sooner item will help reduce misses.
Now with a modified A, if it were changed to use X instead, both behave same otherwise,
the cache keeps y, which is the item that comes back first. 
That cannot create extra misses before Y’s next request, and when Y does show up, 
the modified version gets a hit while A might miss.
Therefore, optff at the first disagreement never increases misses. 
Repeating this swap at every disagreement turns A into optff without increasing misses.
So optff has no more misses than that of ( A ) and is optimal.
