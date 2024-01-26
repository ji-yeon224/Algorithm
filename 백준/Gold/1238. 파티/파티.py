import heapq
import sys

N, M, X = map(int, sys.stdin.readline().split())
MAX = sys.maxsize

go = [MAX for _ in range(N+1)]
back = [MAX for _ in range(N+1)]

dist = {}
redist = {}

for i in range(N):
    dist[i+1] = []
    redist[i+1] = []

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    dist[u].append((v, w))
    redist[v].append((u, w))

def dijkstra(start, result, dist):
    heap = []
    result[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, cur = heapq.heappop(heap)
        if result[cur] < w:
            continue
        for next, nw in dist[cur]:
            nextW = nw + w
            if result[next] > nextW:
                result[next] = nextW
                heapq.heappush(heap, (nextW, next))

    return min(result)

dijkstra(X, back, dist)
dijkstra(X, go, redist)
maxDist = 0
for i in range(1, N+1):
    maxDist = max(go[i] + back[i], maxDist)
print(maxDist)
