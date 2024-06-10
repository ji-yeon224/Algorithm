from collections import deque
import sys
input = sys.stdin.readline

def island(r, c, index):
    global N
    queue = deque([])
    queue.append((r, c))
    visited[r][c] = True
    graph[r][c] = index
    while queue:
        curR, curC = queue.popleft()
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                graph[nr][nc] = index
                queue.append((nr, nc))
    
def bridge(index):
    global N, answer
    dist = [[-1]*N for _ in range(N)]
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if graph[i][j] == index:
                queue.append((i, j))
                dist[i][j] = 0
    while queue:
        curR, curC = queue.popleft()
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] != 0 and graph[nr][nc] != index:
                    answer = min(answer, dist[curR][curC])
                    continue
                if graph[nr][nc] == 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[curR][curC] + 1
                    queue.append((nr, nc))

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

index = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            island(i, j, index)
            index += 1

answer = N*N
for i in range(1, index+1):
    bridge(i)
    
print(answer)