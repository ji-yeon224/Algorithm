from heapq import heappop, heappush
heap = []
N = int(input())

for _ in range(N):
    heappush(heap, int(input()))

answer = 0
while heap:
    if len(heap) == 1:
        print(answer)
        break
    num1 = heappop(heap)
    num2 = heappop(heap)
    answer += (num1 + num2)
    heappush(heap, num1+num2)