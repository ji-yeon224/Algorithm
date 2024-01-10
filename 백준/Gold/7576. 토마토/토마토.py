from collections import deque


m, n = map(int, input().split())
box = [[int(num) for num in input().split()] for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
zeroCnt = 0

queue = deque()

def isPossible(r, c):
    if r >= 0 and r < n and c >= 0 and c < m and box[r][c] == 0:
        return True
    else: return False

def bfs():
    day = 0
    global zeroCnt
    while queue:
        cur = queue.popleft()
        d = cur[2]
        for i in dir:
            nxtR = cur[0] + i[0]
            nxtC = cur[1] + i[1]
            if isPossible(nxtR, nxtC) == True:
                zeroCnt -= 1
                queue.append((nxtR, nxtC, d+1))
                box[nxtR][nxtC] = d+1
                day = max(day, d+1)
    return day
            
def solution():
    global zeroCnt
    for arr in enumerate(box):
        for value in enumerate(arr[1]):
            if value[1] == 1:
                queue.append((arr[0], value[0], 0))
            elif value[1] == 0:
                zeroCnt += 1

    if zeroCnt == 0: return 0

    day = bfs()
    if zeroCnt > 0:
        return -1
    
    return day 
    
print(solution())
    
