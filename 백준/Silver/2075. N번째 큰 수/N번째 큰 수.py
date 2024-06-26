from heapq import heappush, heappop

N = int(input())
heap = []
for _ in range(N):
    arr = list(map(int, input().split()))
    for n in arr:
        if len(heap) < N:
            heappush(heap, n)
        else:
            if heap[0] < n:
                heappop(heap)
                heappush(heap, n)

print(heappop(heap))
