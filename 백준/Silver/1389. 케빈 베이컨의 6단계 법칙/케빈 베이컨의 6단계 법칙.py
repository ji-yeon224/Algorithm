from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
def bfs(user):
    queue = deque([(user, 0)])
    visited = [False]*(n+1)
    visited[user] = True
    result = 0
    while queue:
        cur = queue.popleft()
        result += cur[1]
        for i in arr[cur[0]]:
            if visited[i] == False:
                visited[i] = True
                queue.append((i, cur[1]+1))
    return result
    
result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)