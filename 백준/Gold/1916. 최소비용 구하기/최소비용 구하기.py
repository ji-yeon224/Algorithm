import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, dest, cost = map(int, sys.stdin.readline().split())
    graph[start].append((dest, cost)) # 목적지, 비용    

def dijkstra(graph, start, dest):
    heap = []
    dist = [sys.maxsize] * (N+1)
    dist[start] = 0
    heapq.heappush(heap, (0, start)) # 비용, 위치 -> 비용 기준 최소 힙
    while heap:
        cost, cur = heapq.heappop(heap)

        if dist[cur] < cost:
            continue

        for next in graph[cur]:
            nextCost = cost + next[1]
            nxtIdx = next[0]
            if dist[nxtIdx] > nextCost:
                dist[nxtIdx] = nextCost
                heapq.heappush(heap, (nextCost, nxtIdx))
    
    return dist[dest]
        
start, dest = map(int, sys.stdin.readline().split())
print(dijkstra(graph, start, dest))