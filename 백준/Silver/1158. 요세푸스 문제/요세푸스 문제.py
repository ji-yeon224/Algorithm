from collections import deque
N, K = map(int, input().split())
numList = [i for i in range(1, N+1)]
queue = deque(numList)
answer = []

while queue:
    for _ in range(K-1):
        num = queue.popleft()
        queue.append(num)
    answer.append(queue.popleft())
print("<", end="")
print(", ".join(map(str, answer)), end="")
print(">")