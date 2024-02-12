
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

dict = {}
    
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 in dict:
        dict[v1].append(v2)
    else:
        dict[v1] = [v2]
    if v2 in dict:
        dict[v2].append(v1)
    else:
        dict[v2] = [v1]
        
def bfs():
    result = [V]
    visited = [False]*(N+1)
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        cur = queue.popleft()
        nextNode = sorted(dict[cur])
        for nxt in nextNode:
            if not visited[nxt]:
                queue.append(nxt)
                result.append(nxt)
                visited[nxt] = True
    
    return " ".join(map(str, result))


result = [V]
visited = [False]*(N+1)
visited[V] = True

def dfs(cur):
    for nxt in sorted(dict[cur]):
        if not visited[nxt]:
            visited[nxt] = True
            result.append(nxt)
            dfs(nxt)

if V not in dict:
    print(V)
    print(V)
else:
    dfs(V)
    print(" ".join(map(str, result)))
    print(bfs())
   
 
