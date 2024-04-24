from heapq import heappush, heappop, heapify
from collections import deque
import sys
input = sys.stdin.readline

N, K, T = map(int, input().split())
graph = list(map(int, input().split()))

heap = graph
heapify(heap)

stack = deque()
answer = 0
for i in range(K):
    while heap:
        if heap[0] < T:
            stack.append(heappop(heap))
        else:
            break
    if not stack:
        break
    else:
        T += stack.pop()
    
print(T)    
