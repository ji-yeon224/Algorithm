
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
move = [0]*100001

def bfs():
    queue = deque([N])
    visited = [int(1e9)] * 100001
    visited[N] = 0
    
    while queue:
        cur = queue.popleft()
        
        if cur == K:
            break
        
        for nxt in (cur*2, cur+1, cur-1):
            if nxt >=0 and nxt < 100001 and visited[nxt] > visited[cur]+1:
                visited[nxt] = visited[cur]+1
                queue.append(nxt)
                move[nxt] = cur
    return visited[K]        


result = []
if N > K:
    time = N-K
    print(str(time))
    for i in range(time+1):
        result.append(N-i)
    print(" ".join(map(str, result)))
elif N == K:
    print(0)
    print(N)
    
else:
    result.append(K)
    time = bfs()
    print(time)
    
    cur = K
    while cur != N:
        result.insert(0, move[cur])
        cur = move[cur]
    print(" ".join(map(str, result)))


