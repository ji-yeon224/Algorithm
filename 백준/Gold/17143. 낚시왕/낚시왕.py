import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
graph = [[0]*(C+1) for _ in range(R+1)]
result = 0
dir = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

def getFish(c):
    for i in range(1, R+1):
        if graph[i][c] != 0:
            size = graph[i][c][2]
            graph[i][c] = 0
            return size
    return 0

def moveFish(r, c, s, d):
    nxtR = r
    nxtC = c
    while s > 0:
        nxtR = r + dir[d][0]
        nxtC = c + dir[d][1]
        if nxtR > R or nxtR <= 0 or nxtC > C or nxtC <= 0:
            if d == 1 or d == 3:
                d += 1
            else:
                d -= 1
        else:
            r = nxtR
            c = nxtC
            s -= 1
    return (nxtR, nxtC, d)

def refreshGraph():
    global graph
    fishCnt = 0
    newGraph = [[0]*(C+1) for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            if graph[i][j] != 0:
                fishCnt += 1
                info = graph[i][j]
                nxtR, nxtC, nxtD = moveFish(i, j, info[0], info[1])
                if newGraph[nxtR][nxtC] != 0:
                    newGraph[nxtR][nxtC] = max(newGraph[nxtR][nxtC], (info[0], nxtD, info[2]), key = lambda x: x[2])
                else:
                    newGraph[nxtR][nxtC] = (info[0], nxtD, info[2])
        if fishCnt == M:
                break
    graph = newGraph


for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    graph[r][c] = (s, d, z)


for i in range(1, C+1):
    result += getFish(i)
    refreshGraph()
print(result)