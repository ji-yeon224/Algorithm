
import sys
from collections import deque

input = sys.stdin.readline

case = 0

def printAnswer(case, count):
    if count == 0:
        print("Case {}: No trees.".format(case))
    elif count == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, count))

def bfs(start):
    isTree = True
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        if visited[cur]:
            isTree = False
        visited[cur] = True
        for nxt in dict[cur]:
            if not visited[nxt]:
                queue.append(nxt)
    return isTree

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    answer = 0
    case += 1
    
    dict = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    visited = [False for _ in range(N+1)]
    for i in range(1, N+1):
        if not visited[i]:
            if bfs(i) is True:
                answer += 1
    printAnswer(case, answer)
 