
import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
dict = {}
for i in range(1, N+1):
    dict[i] = []
for i in range(E):
    a, b, c = map(int, input().split())
    dict[a].append((b, c))
    dict[b].append((a, c))
v1, v2 = map(int, input().split())

dist_v1 = [int(1e9)]*(N+1)
dist_v2 = [int(1e9)]*(N+1)


def dijkstra(start, distance):
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist:
            continue
        
        for nxt, nxtd in dict[cur]:
            newDist = dist + nxtd
            
            if newDist < distance[nxt]:
                distance[nxt] = newDist
                heapq.heappush(heap, (newDist, nxt))
    
dist_v1[v1] = 0
dist_v2[v2] = 0
dijkstra(v1, dist_v1)
dijkstra(v2, dist_v2)

result = min(dist_v1[1] + dist_v1[v2] + dist_v2[N], dist_v2[1] + dist_v2[v1] + dist_v1[N])
if result >= int(1e9):
    print(-1)
else: print(result)
