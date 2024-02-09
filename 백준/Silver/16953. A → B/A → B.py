import sys
from collections import deque
A, B = map(int, sys.stdin.readline().split())

queue = deque([(A, 1)])
result = -1
while queue:
    curNum, cnt = queue.popleft()
    if curNum == B:
        result = cnt
        break
    
    for next in [curNum*2, (curNum*10)+1]:
        if next <= B:
            queue.append((next, cnt+1))
            
print(result)