from FIFO import fifo
from LRU import lru
from OPTFF import optff
import sys

def main():
    k, m = map(int, input().split())
    requests = list(map(int, input().split()))

    print(f"FIFO  : {fifo(k, requests)}")
    print(f"LRU   : {lru(k, requests)}")
    print(f"OPTFF : {optff(k, requests)}")

if __name__ == "__main__":
    main()