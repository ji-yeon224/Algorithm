N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer = [-1]*(N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == graph[j][i] == INF:
            answer[i] += 1

for i in range(1, N+1):
    print(answer[i])