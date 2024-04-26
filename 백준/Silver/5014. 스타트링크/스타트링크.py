
from collections import deque
F, S, G, U, D = map(int, input().split())

visited = [False]*(F+1)
visited[S] = True

queue = deque()
queue.append((S, 0))
isPossible = False
while queue:
    cur, move = queue.popleft()
    if cur == G:
        isPossible = True
        print(move)
        break
    for nxt in (cur+U, cur-D):
        if 0 < nxt <= F and not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, move+1))
    if isPossible:
        break
    
if not isPossible:
    print("use the stairs")