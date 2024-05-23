from collections import deque
N = int(input())

def bfs(start):
    total = 0
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        cur, level = queue.popleft()
        total = max(level, total)
        for friend in relation[cur]:
            if not visited[friend]:
                queue.append((friend, level + 1))
                visited[friend] = True
    
    return total

relation = {i: [] for i in range(1, N+1)}
while True:
    f1, f2 = map(int, input().split())
    if f1 == -1 and f2 == -1:
        break
    relation[f1].append(f2)
    relation[f2].append(f1)

levelList = [0]*(N+1)
minLevel = N
for i in range(1, N+1):
    visited = [False] *(N+1)
    level = bfs(i)
    minLevel = min(level, minLevel)
    levelList[i] = level
    
print(minLevel, levelList.count(minLevel))
for i in range(1, N+1):
    if levelList[i] == minLevel:
        print(i, end = ' ')