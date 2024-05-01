from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))

robot = deque([False]*N)
level = 0
zeroCnt = 0

while True:
    level += 1
    belt.rotate(1)
    robot.rotate(1)
    # print(belt)
    robot[N-1] = False
    
    for i in range(N-2, -1, -1):
        if robot[i] == True:
            if not robot[i+1] and belt[i+1] > 0:
                belt[i+1] -= 1
                robot[i] = False
                robot[i+1] = True
                
    robot[N-1] = False
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1        
    if belt.count(0) >= K:
        break
print(level)