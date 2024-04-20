import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
maxNum = 1


graph = []
for _ in range(N):
    tmp = [n for n in map(int, input().split())]
    graph.append(tmp)
    maxNum = max(maxNum, max(tmp))

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]   
def bfs(r, c, h):
    queue = deque()
    queue.append((r, c))
    
    while queue:
        curR, curC = queue.popleft()
        
        for dr, dc in dir:
            nxtR = curR + dr
            nxtC = curC + dc
            if 0 <= nxtR < N and 0 <= nxtC < N and graph[nxtR][nxtC] > h and not visited[nxtR][nxtC]:
                visited[nxtR][nxtC] = True
                queue.append((nxtR, nxtC))


answer = 0

for h in range(maxNum):
    visited = [[False]*N for _ in range(N)]
    area = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                visited[i][j] = True
                bfs(i, j, h)
                area += 1
    
    answer = max(answer, area)
print(answer)