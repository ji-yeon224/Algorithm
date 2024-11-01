import sys
input = sys.stdin.readline

N = int(input())
numList = {i: int(input()) for i in range(1, N+1)}
results = []
visited = [False]*(N+1)

def dfs(node, visitList):
    visited[node] = True
    nextNode = numList[node]
    if visited[nextNode]: #다음 노드를이미 방문 했으면
        if visitList[0] == nextNode:
            results.extend(visitList)
    else:
        dfs(nextNode, visitList+[nextNode])
    
for i in range(1, N+1):
    if i not in results:
        dfs(i, [i])
        visited = [False]*(N+1)
print(len(results))
results.sort()
print(*results, sep="\n")