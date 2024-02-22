import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 방문여부, 벽


def bfs():
    queue = deque([(0, 0, 0)])
    
    while queue:
        curR, curC, wall = queue.popleft()
        
        if curR == N-1 and curC == M-1:
            return visited[curR][curC][wall]+1
            
        for d in dir:
            nxtR = curR + d[0]
            nxtC = curC + d[1]
            if nxtR >= 0 and nxtR < N and nxtC >= 0 and nxtC < M:
                
                if graph[nxtR][nxtC] == 1 and wall == 0:
                    # 벽인데 이전에 안부수고 왔을 경우
                    queue.append((nxtR, nxtC, 1))
                    visited[nxtR][nxtC][1] = visited[curR][curC][0]+1
                    
                elif graph[nxtR][nxtC] == 0 and visited[nxtR][nxtC][wall] == 0:
                    queue.append((nxtR, nxtC, wall))
                    visited[nxtR][nxtC][wall] = visited[curR][curC][wall]+1
    
    return -1

print(bfs())