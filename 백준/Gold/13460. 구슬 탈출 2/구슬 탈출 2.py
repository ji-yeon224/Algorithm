import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[c for c in map(str, input().rstrip())] for _ in range(N)]

bIdx = (0, 0)
rIdx = (0, 0)

for i in range(N):
    if 'B' in graph[i]:
        bIdx = (i, graph[i].index('B'))
    if 'R' in graph[i]:
        rIdx = (i, graph[i].index('R'))

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def move(idx, direction):
    r, c = idx
    dirR, dirC = direction
    cnt = 0
    while True:
        if graph[r+dirR][c+dirC] == "#" or graph[r][c] == "O":
            break
        r += dirR
        c += dirC
        cnt += 1
    return (r, c, cnt)


def bfs():
    rr, rc = rIdx
    br, bc = bIdx
    queue = deque([(rr, rc, br, bc, 1)])
    visited[rr][rc][br][bc] = True
    cnt = 0
    
    while queue:
        redR, redC, blueR, blueC, cnt = queue.popleft()
        if cnt > 10:
            break
        
        for d in dir:
            nRedR, nRedC, rCnt = move((redR, redC), d)
            nBlueR, nBlueC, bCnt = move((blueR, blueC), d)
            if graph[nBlueR][nBlueC] == 'O':
                continue
            if graph[nRedR][nRedC] == 'O':
                print(cnt)
                return
            
            if nRedR == nBlueR and nRedC == nBlueC:
                if rCnt > bCnt:
                    nRedR -= d[0]
                    nRedC -= d[1]
                else:
                    nBlueR -= d[0]
                    nBlueC -= d[1]
                
            if not visited[nRedR][nRedC][nBlueR][nBlueC]:
                visited[nRedR][nRedC][nBlueR][nBlueC] = True
                queue.append((nRedR, nRedC, nBlueR, nBlueC, cnt+1))
    print(-1)
bfs()