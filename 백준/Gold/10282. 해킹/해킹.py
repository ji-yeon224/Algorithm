import sys
import heapq

T = int(sys.stdin.readline())
INF = int(1e9)

def solution():
    N, D, C = map(int, sys.stdin.readline().split())
    
    dict = {}
    for i in range(1, N+1):
        dict[i] = []
    
    for _ in range(D):
        a, b, s = map(int, sys.stdin.readline().split())
        dict[b].append((a, s))
        
    visited = [INF]*(N+1)
    visited[C] = 0
    heap = [(0, C)]
    heapq.heapify(heap)
    while heap:
        time, com = heapq.heappop(heap)
        if time > visited[com]:
            continue
        
        for c, t in dict[com]:
            
            if visited[c] > visited[com]+t:
                visited[c] = visited[com]+t
                heapq.heappush(heap, (t, c))
    idx = 0
    time = 0
    for i, t in enumerate(visited):
        if t < INF:
            idx += 1
            if  t > time:
                time = t
                
    print(idx, time)
    
for _ in range(T):
    solution()
