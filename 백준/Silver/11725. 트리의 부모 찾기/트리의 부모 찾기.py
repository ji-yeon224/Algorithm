
import sys
from collections import deque

N = int(sys.stdin.readline())
dict = {}

for i in range(1, N+1):
    dict[i] = []

for i in range(N-1):
    n1, n2 =  map(int, sys.stdin.readline().split())
    dict[n1].append(n2)
    dict[n2].append(n1)

def bfs():
    parents = [0]*(N+1)
    queue = deque([1])
    parents[1] = -1
    
    while queue:
        cur = queue.popleft()
        
        
        for child in dict[cur]:
            if child == 1 or parents[child] > 0:
                continue
            parents[child] = cur
            queue.append(child)
    
    return parents[2:]


parents = bfs()
for n in parents:
    print(n)