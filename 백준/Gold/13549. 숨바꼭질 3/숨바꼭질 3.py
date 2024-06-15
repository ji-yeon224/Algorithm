import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())


visited = [-1] * 100001

def bfs(n, k):
    queue = deque([n])
    visited[n] = 0
    while queue:
        cur = queue.popleft()
        if cur == k:
            print(visited[cur])
            break
        
        if cur*2 <= 100000 and visited[cur*2] == -1:
            queue.appendleft(cur*2)
            visited[cur*2] = visited[cur]
        
        for move in (cur - 1, cur + 1):
            if move > -1 and move <= 100000 and visited[move] == -1:
                queue.append(move)
                visited[move] = visited[cur]+1



bfs(N, K)