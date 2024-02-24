import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [i for i in range(1,N+1)]

stack = deque(arr)

while len(stack)>1:
    stack.popleft()
    last = stack.popleft()
    stack.append(last)
    
print(stack.pop())  