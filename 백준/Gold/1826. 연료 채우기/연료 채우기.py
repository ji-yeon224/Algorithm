import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
oils = []
for _ in range(N):
    a, b = map(int, input().split())
    oils.append((a, b))
oils.sort(key = lambda x : (x[0], -x[1]))

dest, curFuel = map(int, input().split())
oils.append((dest, 0))
stop = 0
heap = []

for dist, fuel in oils:
    
    if curFuel >= dest:
        break
    while curFuel < dist and heap:
        curFuel += -heappop(heap)
        stop += 1
    if curFuel < dist:
        break
    heappush(heap, -fuel)
    
print(stop if curFuel >= dest else -1)