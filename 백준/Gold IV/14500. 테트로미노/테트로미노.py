import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[n for n in map(int, sys.stdin.readline().split())] for _ in range(N)]
visited = [[False]*M for _ in range(N)]

maxSum = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(cnt, total, curR, curC):
    global maxSum
    
    if cnt == 3:
        maxSum = max(maxSum, total)
        return
        
    for r, c in dir:
        nxtR = curR + r
        nxtC = curC + c
        if nxtR >= 0 and nxtC >= 0 and nxtR < N and nxtC < M and not visited[nxtR][nxtC]:
            visited[nxtR][nxtC] = True
            dfs(cnt+1, total+graph[nxtR][nxtC], nxtR, nxtC)
            visited[nxtR][nxtC] = False
            if cnt == 1:
                visited[nxtR][nxtC] = True
                dfs(cnt+1, total+graph[nxtR][nxtC], curR, curC)
                visited[nxtR][nxtC] = False
  

    
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(0, graph[i][j], i, j)
        visited[i][j] = False
    
print(maxSum)
    
    
