from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        cur = queue.popleft()
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
    
N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = [False]*(N+1)
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        answer += 1
print(answer)
