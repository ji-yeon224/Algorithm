from collections import deque

def bfs(r, c):
    global N, M
    queue = deque([(r, c)])
    size = 1
    while queue:
        curR, curC = queue.popleft()
        for dr, dc in dirs:
            nxtR = curR + dr
            nxtC = curC + dc
            if 0 <= nxtR < N and 0 <= nxtC < M and graph[nxtR][nxtC] == 1 and not visited[nxtR][nxtC]:
                visited[nxtR][nxtC] = True
                queue.append((nxtR, nxtC))
                size += 1
    return size

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxSize = 0
picture = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            maxSize = max(maxSize, bfs(i, j))
            picture += 1
print(picture)
print(maxSize)