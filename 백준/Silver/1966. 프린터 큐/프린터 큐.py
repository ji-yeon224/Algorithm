import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for i in range(T):
    N, dest = map(int, input().split())
    
    queue = deque(list(map(int, input().split())))
    count = 0
    
    while queue:
        top = max(queue)
        front = queue.popleft()
        dest -= 1
        if front < top:
            queue.append(front)
            if dest < 0:
                dest = len(queue)-1
        else:
            count += 1
            if dest < 0:
                print(count)
                break
