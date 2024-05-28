from collections import deque

def bfs(r, c):
    global destR, destC
    queue = deque([])
    queue.append((r, c))
    result = "sad"
    while queue:
        curR, curC = queue.popleft()
        if abs(destR - curR) + abs(destC - curC) <= 1000:
            result = "happy"
            break
        for index, shop in enumerate(shops):
            if abs(shop[0] - curR) + abs(shop[1] - curC) <= 1000 and not visited[index]:
                visited[index] = True
                queue.append(shop)
    print(result)

t = int(input())
for _ in range(t):
    n = int(input())
    startR, startC = map(int, input().split())
    shops = []
    for _ in range(n):
        r, c = map(int, input().split())
        shops.append((r, c))
    destR, destC = map(int, input().split())
    visited = [False]*n
    bfs(startR, startC)