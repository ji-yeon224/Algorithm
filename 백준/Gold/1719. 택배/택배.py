
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]
res = [["-"]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a][b] = w
    graph[b][a] = w
    res[a][b] = str(b)
    res[b][a] = str(a)


def dijkstra(start):
    global res, graph
    heap = []
    for i in range(1, N+1):
        if i == start:
            continue
        heapq.heappush(heap, (graph[start][i], i))
    
    while heap:
        time, curNode = heapq.heappop(heap)
        if graph[start][curNode] < time:
            continue
        for i in range(1, N+1):
            if i == start or i == curNode:
                continue
            
            if graph[start][i] > time + graph[curNode][i]:
                graph[start][i] = time + graph[curNode][i]
                res[start][i] = res[start][curNode]
                heapq.heappush(heap, (time + graph[curNode][i], i))
                
        
for i in range(1, N+1):
    dijkstra(i)

for i in range(1, N+1):
    print(" ".join(res[i][1:]))
  