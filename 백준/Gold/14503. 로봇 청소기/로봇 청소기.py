import sys
input = sys.stdin.readline

N, M = map(int, input().split())
curR, curC, curDir = map(int, input().split())
graph = [[n for n in map(int, input().split())] for _ in range(N)]
cleaned = [[False]*M for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cleaned[curR][curC] = True
answer = 1

def changeDir():
    global curDir
    if curDir == 0:
        curDir = 3
    else:
        curDir -= 1

turnCnt = 0
while True:
    changeDir()
    
    
    nxtR = curR + dir[curDir][0]
    nxtC = curC + dir[curDir][1]
    if graph[nxtR][nxtC] == 0 and not cleaned[nxtR][nxtC]:
        cleaned[nxtR][nxtC] = True
        curR = nxtR
        curC = nxtC
        turnCnt = 0
        answer += 1
        
        continue
    else:
        turnCnt += 1
    
    if turnCnt == 4:
        nxtR = curR - dir[curDir][0] 
        nxtC = curC - dir[curDir][1]
        
        if graph[nxtR][nxtC] == 1:
            print(answer)
            break
        else:
            turnCnt = 0
            curR = nxtR
            curC = nxtC