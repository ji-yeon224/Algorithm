N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [False] * (N+1)
visited[1] = True
for friend in graph[1]:
    if not visited[friend]:
        visited[friend] = True
        answer += 1
    for ff in graph[friend]:
        if not visited[ff]:
            answer += 1
            visited[ff] = True
print(answer)