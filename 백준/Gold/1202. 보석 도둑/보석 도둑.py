import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().split())

jewel = [list(map(int, input().split())) for _ in range(N)]
jewel.sort()

bag = [int(input()) for _ in range(K)]
bag.sort()

result = 0
heap = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        heappush(heap, -jewel[0][1])
        heappop(jewel)
    if heap:
        result -= heappop(heap)
    
print(result)