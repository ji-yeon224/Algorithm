from collections import deque

N, L = map(int, input().split())
numList = list(map(int, input().split()))
queue = deque([(0, numList[0])])
print(numList[0], end = ' ')
for i in range(1, N):
    if queue and queue[0][0] <= i-L:
        queue.popleft()
    while queue and queue[-1][1] > numList[i]:
        queue.pop()
    queue.append((i, numList[i]))
    print(queue[0][1], end = ' ')