
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

def topology(W, N, degrees, times, dict):
    queue = deque()
    total = [0]*(N+1)
    for i in range(1, N+1):
        if degrees[i] == 0:
           queue.append(i) 
           total[i] = times[i]
    
    while queue:
        cur = queue.popleft()
        
        if cur == W:
            print(total[cur])
            break
        
        for nxt in dict[cur]:
            total[nxt] = max(total[nxt], total[cur] + times[nxt])
            degrees[nxt] -= 1
            if degrees[nxt] == 0:
                queue.append(nxt)

def solution():
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.insert(0, 0)
    dict = {i: [] for i in range(1, N+1)}
    degrees = [0]*(N+1)
    
    for _ in range(K):
        X, Y = map(int, input().split())
        dict[X].append(Y)
        degrees[Y] += 1
    W = int(input())
    topology(W, N, degrees, times, dict)

for _ in range(T):
    solution()
