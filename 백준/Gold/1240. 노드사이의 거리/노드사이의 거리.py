from collections import deque

N, M = map(int, input().split())
graph = {i:[] for i in range(N+1)}
for _ in range(N-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def dfs(start, dest, dist):
    global count
    if start == dest:
        count = dist
        return
    
    for nxt, nxtD in graph[start]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, dest, dist+nxtD)
        
for _ in range(M):
    start, dest = map(int, input().split())
    visited = [False]*(N+1) 
    visited[start] = True
    count = 0
    dfs(start, dest, count)
    print(count)
    