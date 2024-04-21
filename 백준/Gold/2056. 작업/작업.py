
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = {i: [] for i in range(1, N+1)}
degrees = [0]*(N+1)
times = [0]*(N+1)

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    if tmp[1] == 0:
        continue
    for j in range(2, len(tmp)):
        graph[tmp[j]].append(i)
        degrees[i] += 1

dp = [0]*(N+1) 
queue = deque()
for i in range(1, N+1):
    if degrees[i] == 0:
        queue.append(i)
        dp[i] = times[i]


while queue:
    cur = queue.popleft()
    
    for nxt in graph[cur]:
        degrees[nxt] -= 1
        dp[nxt] = max(dp[cur] + times[nxt], dp[nxt])
        if degrees[nxt] == 0:
            queue.append(nxt)

print(max(dp)) 