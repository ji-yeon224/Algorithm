import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 1e9

M, N = map(int, input().split())
graph = [[int(n) for n in list(input().rstrip())] for _ in range(N)]
wall = [[INF]*M for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

heap = []
heappush(heap, (0, 0, 0))
wall[0][0] = 0

while heap:
    curR, curC, curW = heappop(heap)
    
    if wall[curR][curC] < curW:
        continue
    
    for d in dir:
        nxtR = curR + d[0]
        nxtC = curC + d[1]
        if nxtR >= 0 and nxtR < N and nxtC >= 0 and nxtC < M:
            newState = curW + graph[nxtR][nxtC] # 다음 위치로 가기 위해 부순 벽 갯수 
            if wall[nxtR][nxtC] > newState:
                wall[nxtR][nxtC] = newState
                heappush(heap, (nxtR, nxtC, newState))
    
print(wall[N-1][M-1])