from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        print(heappop(heap)[1] if heap else 0)
    else:
        heappush(heap, (abs(num), num))