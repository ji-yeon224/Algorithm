import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[int(n) for n in sys.stdin.readline().strip().split()] for _ in range(N)]

check = [[0] * M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(queue):
    cheeseSet = set()
    while queue:
        curR, curC = queue.popleft()
        for d in dir:
            nxtR = curR+d[0]
            nxtC = curC+d[1]
            if nxtR >= 0 and nxtR < N and nxtC >= 0 and nxtC < M:
                if graph[nxtR][nxtC] == 0 and not visited[nxtR][nxtC]:
                    visited[nxtR][nxtC] = True
                    queue.append((nxtR, nxtC))
                elif graph[nxtR][nxtC] == 1:
                    check[nxtR][nxtC] += 1
                    if check[nxtR][nxtC] >= 2:
                        cheeseSet.add((nxtR, nxtC))
                        
    return cheeseSet
                
    

cheeseCnt = 0
time = 0
for i in range(N):
    cheeseCnt += graph[i].count(1)


queue = deque([(0, 0)])
while cheeseCnt > 0:
    time += 1
    cheeseSet = bfs(queue)
    
    cheeseCnt -= len(cheeseSet)
    for r, c in cheeseSet:
        graph[r][c] = 0
        visited[r][c] = True
        queue.append((r, c))
    
print(time)
    