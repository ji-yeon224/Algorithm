import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())

numList = [tuple(map(int, input().split())) for _ in range(N)]
numList.sort(key = lambda x: (x[0], x[1]))

count = 1
heap = []
heappush(heap, numList[0][1])

for i in range(1, N):
    start, end = numList[i]
    if heap[0] > start:
        count += 1
    else:
        heappop(heap)
    heappush(heap, end)
    
print(count)