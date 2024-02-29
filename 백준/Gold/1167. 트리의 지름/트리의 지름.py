import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
tree = [[] for _ in range(V+1)]

for i in range(V):
    inputList = [int(i) for i in input().split()]
    node = inputList[0]
    for i in range(1, len(inputList)-1, 2):
        n = inputList[i]
        w = inputList[i+1]
        tree[node].append([n, w])


def bfs(start):
    queue = deque()
    dist = [-1] * (V+1)
    dist[start] = 0
    queue.append((start, 0))
    
    while queue:
        cur, weight = queue.popleft()
        
        for t, w in tree[cur]:
            if dist[t] == -1:
                dist[t] = weight + w
                queue.append((t, weight + w))
                
    return dist           



dist = bfs(1)
start = dist.index(max(dist))

dist = bfs(start)
print(max(dist))