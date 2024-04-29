gears = [list(input()) for _ in range(4)]
K = int(input())
rotate = [list(map(int, input().split())) for _ in range(K)]

def rotateGear(dirList):
    for idx, d in enumerate(dirList):
        if d == 0:
            continue
        elif d == 1:
            last = gears[idx].pop()
            gears[idx].insert(0, last)
        else:
            first = gears[idx].pop(0)
            gears[idx].append(first)
        

for i in range(K):
    gearNum = rotate[i][0] -1
    r = rotate[i][1]
    dirList = [0]*4
    dirList[gearNum] = r
    
    #오른쪽 체크
    for right in range(gearNum + 1, 4):
        
        if gears[right-1][2] == gears[right][6]:
            break
        else:
            dirList[right] = dirList[right-1]*-1
    for left in range(gearNum - 1, -1, -1):
        if gears[left+1][6] == gears[left][2]:
            break
        else:
            dirList[left] = dirList[left+1]*-1
    rotateGear(dirList)
    
answer = 0
for i in range(4):
    if gears[i][0] == '1':
        answer += (2**i)
print(answer)