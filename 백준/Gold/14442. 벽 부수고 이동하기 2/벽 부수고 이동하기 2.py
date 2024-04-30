from collections import deque
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0]*(M) for _ in range(N)] for _ in range(K+1)]
visited[K][0][0] = 1
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()
queue.append((0, 0, K))

answer = -1
while queue:
    
    curR, curC, wall = queue.popleft()
    
    if curR == N-1 and curC == M-1:
        answer = visited[wall][curR][curC]
        break
    
    for dr, dc in dir:
        nxtR = curR + dr
        nxtC = curC + dc
        if 0 <= nxtR < N and 0 <= nxtC < M :
            if graph[nxtR][nxtC] == 1 and wall > 0 and visited[wall-1][nxtR][nxtC] == 0:
                visited[wall-1][nxtR][nxtC] = visited[wall][curR][curC]+1
                queue.append((nxtR, nxtC, wall-1))
            elif graph[nxtR][nxtC] == 0 and visited[wall][nxtR][nxtC] == 0:
                visited[wall][nxtR][nxtC] = visited[wall][curR][curC]+1
                queue.append((nxtR, nxtC, wall))

print(answer)