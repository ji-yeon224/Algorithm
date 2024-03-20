
import sys
from heapq import heappush, heappop

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

visited = [False for _ in range(V+1)]

heap = []
heappush(heap, (0, 1))
result = 0

while heap:
    w, cur = heappop(heap)
    
    if not visited[cur]:
        result += w
        visited[cur] = True
        for nxt, nxtw in graph[cur]:
            heappush(heap, (nxtw, nxt))
    
print(result)