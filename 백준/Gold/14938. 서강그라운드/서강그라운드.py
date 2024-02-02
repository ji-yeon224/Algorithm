import sys
import heapq

N, M, R = map(int, sys.stdin.readline().split())
itemArr = [int(item) for item in sys.stdin.readline().split()]
itemArr.insert(0, 0)
field = {}


for i in range(1, N+1):
    field[i] = []
    
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())
    field[a].append((b, l))
    field[b].append((a, l))


def dijkstra(start):
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist:
            continue
        
        for nxt, d in field[cur]:
            if distance[nxt] > dist+d:
                distance[nxt] = dist+d
                heapq.heappush(heap, (dist+d, nxt))
            

maxItem = 0

for i in range(1, N+1):
    distance = [int(1e9)]* (N+1)
    dijkstra(i)
    
    result = 0
    for j in range(1, N+1):
        if distance[j] <= M:
            result += itemArr[j]
    maxItem = max(maxItem, result)
print(maxItem)

