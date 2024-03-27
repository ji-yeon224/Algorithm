import sys
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, len(order)-1):
        graph[order[i]].append(order[i+1])
        degree[order[i+1]] += 1

def topology():
    global N, graph, degree
    result = []
    queue = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for nxt in graph[cur]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                queue.append(nxt)

    if len(result) != N:
        print(0)
    else:
        for order in result:
            print(order)


topology()