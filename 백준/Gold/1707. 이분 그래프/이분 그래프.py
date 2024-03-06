import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
    
def bfs(start, check, graph, V):
    
    check[start] = 0
    
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        nxtCheck = (check[cur]+1) % 2
        for nxt in graph[cur]:
            if check[nxt] == nxtCheck:
                continue
            elif check[nxt] == -1:
                check[nxt] = nxtCheck
                queue.append(nxt)
            else:
                return "NO"
    return "YES"
    


def solution():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    check = [-1]*(V+1)
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    result = "YES"
    for i in range(1, V+1):
        if check[i] == -1 and len(graph[i]) != 0:
            result = bfs(i, check, graph, V)
            if result == "NO":
                break
    print(result)

for _ in range(K):
    solution()