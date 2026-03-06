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


