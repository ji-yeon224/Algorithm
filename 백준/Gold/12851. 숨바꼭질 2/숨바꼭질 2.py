import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = [-1] * 100001

def bfs():
    queue = deque([N])
    minTime = int(1e9)
    cnt = 0
    visited[N] = 0
    while queue:
        cur = queue.popleft()
        
        if cur == K:
            
            if visited[cur] < minTime:
                cnt = 1
            elif visited[cur] == minTime:
                cnt += 1
            minTime = min(minTime, visited[cur])
            continue
        
        for nxt in (cur+1, cur-1, cur*2):
            if nxt < 100001 and nxt >= 0 and (visited[nxt] == -1 or visited[nxt] == visited[cur]+1):
                queue.append(nxt)
                visited[nxt] = visited[cur] + 1
    print(minTime)
    print(cnt)
    
    
bfs()