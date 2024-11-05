
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()
buildings = 0
for _ in range(N):
    _, height = map(int, input().split())
    while stack and stack[-1] > height:
        lastH = stack.pop()
        buildings+=1
        while stack and stack[-1] == lastH:
            stack.pop()
    if height != 0:
        stack.append(height)
while stack:
    lastH = stack.pop()
    buildings += 1
    while stack and stack[-1] == lastH:
        stack.pop()
    
print(buildings)