import sys

R, C = map(int, sys.stdin.readline().split())
graph = [[c for c in sys.stdin.readline().strip()] for _ in range(R)]

alpha = [False] * 26
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxCnt = 0
def dfs(r, c, cnt):
    global maxCnt
    maxCnt = max(maxCnt, cnt)
    for d in dir:
        nxtR = r + d[0]
        nxtC = c + d[1]
        if nxtR >= 0 and nxtC >= 0 and nxtR < R and nxtC < C:
            char = graph[nxtR][nxtC]
            idx = ord(char) - 65
            if not alpha[idx]:
                alpha[idx] = True
                dfs(nxtR, nxtC, cnt+1)
                alpha[idx] = False
                

idx = ord(graph[0][0])-65
alpha[idx] = True
dfs(0, 0, 1)
print(maxCnt)