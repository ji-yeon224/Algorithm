import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
cctv = []
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서
moves = [
    [],
    [[0], [1], [2], [3]],
    [[1, 3], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 3, 1], [1, 0, 2], [2, 1, 3], [3, 0, 2]],
    [[0, 1, 2, 3]]
    ]
    
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(M):
        if 0 < line[j] < 6:
            cctv.append((line[j], i, j))


def monitor(graph, curR, curC, move):
    global M, M
    
    for m in move:
        nr = curR
        nc = curC   
        while True:
            nr += dir[m][0]
            nc += dir[m][1]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] != 6:
                if graph[nr][nc] == 0:
                    graph[nr][nc] = -1
                else:
                    continue
            else:
                break

answer = int(1e9)
def dfs(count, graph):
    global N, M, answer
    
    if count == len(cctv):
        # print(graph)
        cnt = 0
        for i in range(N):
            cnt += graph[i].count(0)
        answer = min(answer, cnt)
        return
    copyGraph = copy.deepcopy(graph)
    cctvNum, r, c = cctv[count]
    for move in moves[cctvNum]:
        monitor(copyGraph, r, c, move)
        dfs(count + 1, copyGraph)
        copyGraph = copy.deepcopy(graph)
    

dfs(0, graph)
print(answer)