import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
rootNode = list(range(N+1))

def findRootNode(a):
    if a != rootNode[a]:
        rootNode[a] = findRootNode(rootNode[a])
    return rootNode[a]


result = 0
last = 0
for a, b, c in edges:
    
    aRoot = findRootNode(a)
    bRoot = findRootNode(b)
    if aRoot != bRoot:
        rootNode[aRoot] = bRoot
        result += c
        last = c
    
    
print(result - last)