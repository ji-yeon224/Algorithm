from collections import deque

K = int(input())
stack = deque([])
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

answer = 0
while stack:
    answer += stack.pop()
print(answer)
