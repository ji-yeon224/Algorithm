import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())

leftHeap = [] # max
rightHeap = []

for _ in range(N):
    n = int(input())
    
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, -n)
    else:
        heappush(rightHeap, n)
    if leftHeap and rightHeap and -leftHeap[0] > rightHeap[0]:
        l = -heappop(leftHeap)
        r = heappop(rightHeap)
        heappush(leftHeap, -r)
        heappush(rightHeap, l)
    print(-leftHeap[0])