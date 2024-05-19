import sys
from collections import deque


def bfs(start, end):
    queue = deque([])
    visited = [False]*(N+1)
    queue.append((start, 0))
    isFamily = False
    while queue:
        cur, rel = queue.popleft()
        
        if cur == end:
            print(rel)
            isFamily = True
            break
        
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, rel+1))
    if not isFamily:
        print(-1)
        
input = sys.stdin.readline

N = int(input())
dest1, dest2 = map(int, input().split())
M = int(input())
graph = {i:[] for i in range(1, N+1)}

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


bfs(dest1, dest2)