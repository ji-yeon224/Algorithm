import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
enter = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    enter[B]+=1
    if A in dict:
        dict[A].append(B)
    else:
        dict[A] = [B]

queue = deque([])
for i in range(1, N+1):
    if enter[i] == 0:
        queue.append(i)

result = []
while queue:
    cur = queue.popleft()
    result.append(cur)
    if cur in dict:
        for nxt in dict[cur]:
            enter[nxt] -= 1
            if enter[nxt] == 0:
                queue.append(nxt)
            
    
for n in result:
    print(n, end = " ")