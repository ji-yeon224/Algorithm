from collections import deque

def fBfs():
    global R, C
    fqueue = deque()

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'F':
                fVisited[i][j] = 1
                fqueue.append((i, j))
    
    while fqueue:
        curR, curC = fqueue.popleft()
        
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#' and fVisited[nr][nc] == 0:
                fVisited[nr][nc] = fVisited[curR][curC] + 1
                fqueue.append((nr, nc))

def jBfs():
    global R, C
    isEscape = False
    jqueue = deque()

    for i in range(R):
        if "J" in board[i]:
            jIdx = (i, board[i].index('J'))
            jVisited[jIdx[0]][jIdx[1]] = 1
            jqueue.append(jIdx)
    
    while jqueue:
        curR, curC = jqueue.popleft()
        curTime = jVisited[curR][curC]
        if curR == 0 or curR == R-1 or curC == 0 or curC == C-1:
            isEscape = True
            print(curTime)
            break
        for dr, dc in dirs:
            nr = curR + dr
            nc = curC + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#' and jVisited[nr][nc] == 0:
                if fVisited[nr][nc] == 0 or fVisited[nr][nc] > curTime + 1:
                    jVisited[nr][nc] = curTime + 1
                    jqueue.append((nr, nc))
                else:
                    jVisited[nr][nc] = -1
    if not isEscape:
        print("IMPOSSIBLE")

R, C = map(int, input().split())
board = [list(str(input())) for _ in range(R)]

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

fVisited = [[0]*C for _ in range(R)]
jVisited = [[0]*C for _ in range(R)]

fBfs()
jBfs()