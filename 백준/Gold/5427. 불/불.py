from collections import deque

T = int(input())

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start):
    global w, h
    fireQ = deque(fires)
    while fireQ:
        curR, curC = fireQ.popleft()
        curTime = fVisited[curR][curC]
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0<= nr < h and 0 <= nc < w and board[nr][nc] != '#' and fVisited[nr][nc] == INF:
                fVisited[nr][nc] = curTime + 1
                fireQ.append((nr, nc))
                
    escapeQ = deque([(start[0], start[1], 1)])
    isEscape = False
    
    while escapeQ:
        curR, curC, curTime = escapeQ.popleft()
        if curR == 0 or curR == h-1 or curC == 0 or curC == w-1:
            isEscape = True
            print(curTime)
            break
        
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0<= nr < h and 0 <= nc < w and board[nr][nc] == '.' and not visited[nr][nc] and fVisited[nr][nc] > curTime+1:
                escapeQ.append((nr, nc, curTime+1))
                visited[nr][nc] = True
                
    if not isEscape:
        print("IMPOSSIBLE")

for i in range(T):
    w, h = map(int, input().split())
    INF = w*h
    fires = []
    fVisited = [[INF]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    
    board = []
    for r in range(h):
        tmp = list(input())
        for c in range(w):
            if tmp[c] == '@':
                start = (r, c)
                visited[r][c] = True
            elif tmp[c] == '*':
                fires.append((r, c))
                fVisited[r][c] = 1
        board.append(tmp)
    
    bfs(start)