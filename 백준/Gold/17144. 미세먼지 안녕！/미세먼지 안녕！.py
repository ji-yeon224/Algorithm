import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

machine = []
for i in range(R):
    if -1 in room[i]:
        machine.append((i, room[i].index(-1)))
        if len(machine) == 2:
            break

def dustSpread():
    global R, C
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    temp = [[0] * C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                total = 0
                for d in dir:
                    nxtR = i + d[0]
                    nxtC = j + d[1]
                    spread = room[i][j] // 5
                    
                    if nxtR >= 0 and nxtC >= 0 and nxtR < R and nxtC < C and room[nxtR][nxtC] != -1:
                        temp[nxtR][nxtC] += spread
                        total += spread
                room[i][j] -= total # 퍼진 먼지 양 빼기
    for i in range(R):
        for j in range(C):
            room[i][j] += temp[i][j]

def machineOnUp(start):
    global R, C
    dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction = 0
    curR = start[0] + dir[0][0]
    curC = start[1] + dir[0][1]
    prev = 0
    while True:
        if room[curR][curC] == -1:
            break
        tmp = room[curR][curC]
        room[curR][curC] = prev
        prev = tmp
        nxtR = curR + dir[direction][0]
        nxtC = curC + dir[direction][1]
        if nxtR >= 0 and nxtC >= 0 and nxtR < R and nxtC < C:
            curR = nxtR
            curC = nxtC
        else:
            direction += 1
            curR += dir[direction][0]
            curC += dir[direction][1]

def machineOnDown(start):
    global R, C
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    curR = start[0] + dir[0][0]
    curC = start[1] + dir[0][1]
    prev = 0
    while True:
        if room[curR][curC] == -1:
            break
        tmp = room[curR][curC]
        room[curR][curC] = prev
        prev = tmp
        nxtR = curR + dir[direction][0]
        nxtC = curC + dir[direction][1]
        if nxtR >= 0 and nxtC >= 0 and nxtR < R and nxtC < C:
            curR = nxtR
            curC = nxtC
        else:
            direction += 1
            curR += dir[direction][0]
            curC += dir[direction][1]


for i in range(T):
    dustSpread()
    machineOnUp(machine[0])
    machineOnDown(machine[1])

result = 0   
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]
print(result)