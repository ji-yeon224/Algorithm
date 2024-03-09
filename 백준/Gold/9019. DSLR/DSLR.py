import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

def solution():
    A, B = map(int, input().split())
    
    queue = deque([(A, '')])
    visited = [False] * (10000)
    visited[A] = True
    while queue:
        cur, cmd = queue.popleft()
        
        if cur == B:
            print(cmd)
            break
        
        cmdDNum = (cur*2) % 10000
        if not visited[cmdDNum]:
            visited[cmdDNum] = True
            queue.append((cmdDNum, cmd+'D'))
        cmdSNum = cur - 1
        if cur == 0:
            cmdSNum = 9999
        if not visited[cmdSNum]:
            visited[cmdSNum] = True
            queue.append((cmdSNum, cmd+'S'))
        
        cmdLNum = (cur%1000)*10 + (cur//1000)
        if not visited[cmdLNum]:
            visited[cmdLNum] = True
            queue.append((cmdLNum, cmd+'L'))
        cmdRNum = (cur//10) + (cur%10)*1000
        if not visited[cmdRNum]:
            visited[cmdRNum] = True
            queue.append((cmdRNum, cmd+'R'))
        
for _ in range(T):
    solution()