import sys
from heapq import heappush, heappop
input = sys.stdin.readline
max = int(1e9)

N, M = map(int, input().split())
board = {i : [] for i in range(1, N+1)}

for _ in range(M):
    A, B, C = map(int, input().split())
    board[A].append((B, C))
    board[B].append((A, C))
    
heap = []    
heappush(heap, (0, 1))
dist = [max]*(N+1)
dist[1] = 0
while heap:
    total, cur = heappop(heap)
    if dist[cur] < total:
        continue
    for n, c in board[cur]:
        cost = c + total
        if dist[n] > cost:
            heappush(heap, (cost, n))
            dist[n] = cost
        
print(dist[N])