import sys
from collections import deque

input = sys.stdin.readline

row = 12
col = 6
graph = [list(input().rstrip()) for _ in range(12)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    block.append((r, c))
    color = graph[r][c]
    
    while queue:
        curR, curC = queue.popleft()
        for dr, dc in dir:
            nxtR = curR + dr
            nxtC = curC + dc
            if nxtR >= 0 and nxtR < row and nxtC >= 0 and nxtC < col and not visited[nxtR][nxtC]:
                if graph[nxtR][nxtC] == color:
                    block.append((nxtR, nxtC))
                    queue.append((nxtR, nxtC))
                    visited[nxtR][nxtC] = True
                

def popBlock():
    for r, c in block:
        graph[r][c] = '.'
def down():
    for c in range(col):
        for i in range(10, -1, -1):
            if graph[i][c] == '.':
                continue
            for j in range(11, i, -1):
                if graph[j][c] == '.':
                    graph[j][c] = graph[i][c]
                    graph[i][c] = '.'
                    break
popCnt = 0    
while True:
    isPop = False
    visited = [[False]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if graph[i][j] != '.' and not visited[i][j]:
                block = []
                bfs(i, j)
                if len(block) >= 4:
                    isPop = True
                    popBlock()
                    
    if isPop:
        popCnt += 1
        down()
    else: break
print(popCnt)