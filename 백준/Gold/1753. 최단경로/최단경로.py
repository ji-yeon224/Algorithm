import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

dict = {}
for i in range(V):
    dict[i+1] = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    dict[u].append((v, w))

dist = [int(1e9)]*(V+1)
heap = []
def dijkstra():
    dist[K] = 0
    heapq.heappush(heap, (0, K))

    while heap:
        w, cur = heapq.heappop(heap)
        if dist[cur] < w:
            continue

        for next, nw in dict[cur]:
            nextW = w + nw

            if dist[next] > nextW:
                dist[next] = nextW
                heapq.heappush(heap, (nextW, next))

dijkstra()

for i in range(1, V+1):
    if dist[i] == int(1e9):
        print("INF")
    else:
        print(dist[i])