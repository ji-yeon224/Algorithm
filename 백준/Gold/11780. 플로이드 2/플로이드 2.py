import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF] * (N+1) for _ in range(N+1)]
path = [[-1] *(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    path[a][b] = [a]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            newCost = graph[i][k] + graph[k][j]
            if newCost < graph[i][j]:
                graph[i][j] = newCost
                path[i][j] = path[i][k] + path[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print("")

for i in range(1, N+1):
    for j in range(1, N+1):
        if path[i][j] == -1:
            print(0)
        else:
            print(len(path[i][j])+1, *path[i][j], j)

