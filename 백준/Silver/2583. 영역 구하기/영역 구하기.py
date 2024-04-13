import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*N for _ in range(M)]
def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    size = 1
    
    while queue:
        curR, curC = queue.popleft()
        
        for dr, dc in dir:
            nxtR = curR + dr
            nxtC = curC + dc
            if nxtR >= 0 and nxtR < M and nxtC >= 0 and nxtC < N and graph[nxtR][nxtC] == 0 and not visited[nxtR][nxtC]:
                visited[nxtR][nxtC] = True
                queue.append((nxtR, nxtC))
                size += 1
    return size    


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] += 1

count = 0
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            count += 1
            size = bfs(i, j)
            result.append(size)
result.sort()
print(count)
print(' '.join(map(str, result)))