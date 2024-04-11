import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[n for n in map(int, input().split())] for _ in range(N)]
years = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(sr, sc):
    global graph, N, M
    
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True
    
    while queue:
        curR, curC = queue.popleft()
        seaSide = 0
        for d in dir:
            nxtR = curR + d[0]
            nxtC = curC + d[1]
            if nxtR >= 0 and nxtR < N and nxtC >= 0 and nxtC < M:
                if graph[nxtR][nxtC] == 0:
                    seaSide += 1
                elif not visited[nxtR][nxtC]:
                    visited[nxtR][nxtC] = True
                    queue.append((nxtR, nxtC))
        if seaSide > 0:
            changeList.append((curR, curC, seaSide))
    return 1

while True:
    visited = [[False]*M for _ in range(N)]
    changeList = []
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                iceberg += bfs(i, j)
    
    for r, c, s in changeList:
        graph[r][c] -= s
        if graph[r][c] < 0:
            graph[r][c] = 0
    if iceberg == 0:
        print(0)
        break
    elif iceberg >= 2:
        print(years)
        break
    years += 1