from heapq import heappop, heappush

N = int(input())
arr = []
for _ in range(N):
    d, c = map(int, input().split())
    arr.append((d, c))
arr.sort()

heap = []
answer = 0
for d, c in arr:
    heappush(heap, c)
    answer += c
    if d < len(heap):
        answer -= heappop(heap)    
print(answer)