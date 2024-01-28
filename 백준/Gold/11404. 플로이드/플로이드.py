import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = sys.maxsize

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]


for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, N+1):
    for j in range(1, N+1):
        n = graph[i][j]
        if n == INF:
            print(0, end = " ")
        else:
            print(n, end = " ")
    print("")