import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()
buildings = 0
for _ in range(N):
    a, b = map(int, input().split(' '))
    if not stack:
        if b != 0:
            stack.append((a, b))
    else:
        if stack[-1][1] > b:
            last = stack[-1][1]
            stack.pop()
            buildings += 1
            while stack and stack[-1][1] > b:
                if last != stack[-1][1]:
                    buildings += 1
                    last = stack[-1][1]
                stack.pop()
            if b != 0:
                stack.append((a, b))
        else:
            stack.append((a, b))
if stack:
    lastH = stack[-1][1]
    stack.pop()
    buildings += 1
    while stack:
        if lastH > stack[-1][1]:
            lastH = stack[-1][1]
            buildings += 1
        stack.pop()

print(buildings)