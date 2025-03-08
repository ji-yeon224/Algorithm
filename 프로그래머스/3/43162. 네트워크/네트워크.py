from collections import deque
visited = []
dict = {}

def bfs(start):
    global visited, dict
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()
        for nxt in dict[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                
def solution(n, computers):
    global visited, dict
    network = 0
    visited = [False]*n
    dict = {i: [] for i in range(n)}
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                dict[i].append(j)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            network += 1
                
    return network