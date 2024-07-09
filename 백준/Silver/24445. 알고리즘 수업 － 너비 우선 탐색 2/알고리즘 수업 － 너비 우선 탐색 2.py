from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
queue = deque([R])
visited[R] = 1
index = 1
while queue:
    cur = queue.popleft()
    nxtList = graph[cur]
    nxtList.sort(reverse = True)
    for nxt in nxtList:
        if visited[nxt] == 0:
            queue.append((nxt))
            index += 1
            visited[nxt] = index
for i in range(1, N+1):
    print(visited[i])