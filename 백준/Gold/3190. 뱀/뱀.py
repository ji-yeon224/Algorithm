
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r][c] = True
    
L = int(input())

changeDir = []
for _ in range(L):
    X, C = map(str, input().split())
    changeDir.append((int(X), C))
changeDir.append((100001, ''))
curDir = 0
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def turnDirection(d):
    global curDir
    if d == "L":
        if curDir == 0:
            curDir = 3
        else:
            curDir -= 1
    elif d == "D":
        if curDir == 3:
            curDir = 0
        else:
            curDir += 1



time = 0
curR = 1
curC = 1

queue = deque()
queue.append((1, 1))

move = True # false면 이동 불가
for X, C in changeDir:
    dr, dc = dir[curDir]
    start = time+1
    
    for _ in range(start, X+1):
        time += 1
        nxtR = curR + dr
        nxtC = curC + dc
        
        if nxtR > 0 and nxtR < N+1 and nxtC > 0 and nxtC < N+1 and (nxtR, nxtC) not in queue:
            queue.append((nxtR, nxtC))
            if graph[nxtR][nxtC]:
                graph[nxtR][nxtC] = False
            else:
                queue.popleft()
            curR = nxtR
            curC = nxtC
        else: # 벽이나 몸에 부딪힘
            move = False
            break
    if not move:
        break
    
    turnDirection(C)
     

print(time)