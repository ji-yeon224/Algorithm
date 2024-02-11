
import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)

dict = {}
for i in range(1, n+1):
    dict[i] = []
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    dict[a].append((b, w))


A, B = map(int, sys.stdin.readline().split())
dist = [INF]*(n+1)
route = [0]*(n+1)

heap = []
heapq.heappush(heap, (0, A))
dist[A] = 0

while heap:
    cost, cur = heapq.heappop(heap)
    
    if cost > dist[cur]:
        continue
    
    for n, c in dict[cur]:
        nxtCost = cost + c
        if dist[n] > nxtCost:
            dist[n] = nxtCost
            heapq.heappush(heap, (nxtCost, n))
            route[n] = cur
            
cur = B
result = [cur]
while cur != A:
    result.insert(0, route[cur])
    cur = route[cur]

print(dist[B])
print(len(result))
print(' '.join(map(str, result)))
