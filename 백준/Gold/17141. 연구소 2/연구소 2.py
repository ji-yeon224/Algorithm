from itertools import combinations
from collections import deque

def bfs():
    global N, M, empty
    maxTime = 0
    virusCnt = M
    while queue:
        r, c = queue.popleft()
        time = visited[r][c]
        maxTime = max(maxTime, time)
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 1 and visited[nr][nc] < 0 :
                virusCnt += 1
                visited[nr][nc] = time + 1
                queue.append((nr, nc))
    if virusCnt < empty:
        return INF
    return maxTime

N, M = map(int, input().split())
virus = []
graph = []
empty = 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = N*N
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            empty += 1
            virus.append((i, j))
        elif tmp[j] == 0:
            empty += 1
    graph.append(tmp)

answer = INF
for v in combinations(virus, M):
    queue = deque(v)
    visited = [[-1]*(N+1) for _ in range(N+1)]
    for r, c in v:
        visited[r][c] = 0
    time = bfs()
    answer = min(answer, time)
        
if answer == INF:
    print(-1)
else: 
    print(answer)