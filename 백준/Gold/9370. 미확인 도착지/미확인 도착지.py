import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

T = int(input())

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = []
    heappush(heap, (0, start))
    
    while heap:
        curDist, cur = heappop(heap)
        if curDist > dist[cur]:
            continue
        
        for nxt, nxtDist in dict[cur]:
            newDist = nxtDist + dist[cur]
            if dist[nxt] > newDist:
                dist[nxt] = newDist
                heappush(heap, (newDist, nxt))
    return dist

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    dict = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        a, b, d = map(int, input().split())
        dict[a].append((b, d))
        dict[b].append((a, d))
    dest = []
    for _ in range(t):
        dest.append(int(input()))
        
    startS = dijkstra(s)
    startG = dijkstra(g)
    startH = dijkstra(h)
    
    result = []
    for d in dest:
        minToD = startS[d]
        
        GtoD = startG[d] + startS[h] + startH[g]
        HtoD = startH[d] + startS[g] + startG[h]
        if GtoD == minToD or HtoD == minToD:
            result.append(d)
    result.sort()
    for r in result:
        print(r, end = " ")
            