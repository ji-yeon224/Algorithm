from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
stack = deque([])
for _ in range(N):
    command = list(map(str, input().split()))
    action = command[0]
    if action == "push":
        stack.append(int(command[1]))
    elif action == "pop":
        print(stack.pop() if stack else -1)
    elif action == "size":
        print(len(stack))
    elif action == "empty":
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
