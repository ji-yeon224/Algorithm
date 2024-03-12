import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def topology():
    
    heap = []
    result = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heappush(heap, i)
    while heap:
        cur = heappop(heap)
        result.append(str(cur))
        for nxt in dict[cur]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                heappush(heap, nxt)
    return result




N, M = map(int, input().split())
dict = {i: [] for i in range(1, N+1)}
degree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    dict[A].append(B)
    degree[B] += 1

result = topology()
print(" ".join(result))