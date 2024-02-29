import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])
    tree[c].append([p, w])


def dfs(node, weight):
    
    for n, w in tree[node]:
        if dist[n] == -1:
            dist[n] = w + weight
            dfs(n, w + weight)
            

dist = [-1] * (N+1)
dist[1] = 0
dfs(1, 0)

maxNode = dist.index(max(dist))
dist = [-1] * (N+1)
dist[maxNode] = 0
dfs(maxNode, 0)

print(max(dist))
