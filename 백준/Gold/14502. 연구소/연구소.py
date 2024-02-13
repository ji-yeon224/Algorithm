
import sys
from collections import deque
import copy
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append([int(n) for n in sys.stdin.readline().split()])

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

maxSafe = 0
def bfs():
    global maxSafe
    empty = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                empty.append((i, j))
    
    for combi in combinations(empty, 3):
        copyGraph = copy.deepcopy(graph)
        for wR, wC in combi:
            copyGraph[wR][wC] = 1
        
        queue = deque()
   
    
        for i in range(N):
            for j in range(M):
                if copyGraph[i][j] == 2:
                    queue.append((i, j))
        
        
        while queue:
            curR, curC = queue.popleft()
            
            if copyGraph[curR][curC] != 2:
                continue
            
            for nDir in dir:
                nxtR = curR + nDir[0]
                nxtC = curC + nDir[1]
                if nxtR >= 0 and nxtR < N and nxtC >= 0 and nxtC < M:
                    if copyGraph[nxtR][nxtC] == 0:
                        queue.append((nxtR, nxtC))
                        copyGraph[nxtR][nxtC] = 2
                        
        cnt = 0
        for i in range(N):
            cnt += copyGraph[i].count(0)
        maxSafe = max(maxSafe, cnt)
    
    return maxSafe
    

print(bfs())


