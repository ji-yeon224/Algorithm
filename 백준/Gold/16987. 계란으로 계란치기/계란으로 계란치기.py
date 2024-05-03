
N = int(input())
eggs = [[n for n in map(int, input().split())] for _ in range(N)]

answer = 0

def isBreakCnt(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt

def eggBreak(index):
    global answer, N
    if index == N:
        answer = max(answer, isBreakCnt(eggs))
        return
        
    if eggs[index][0] <= 0:
        eggBreak(index+1)
        return
    
    isBreak = True
    for i in range(N):
        if i == index:
            continue
        if eggs[i][0] > 0:
            isBreak = False
            break
    
    if isBreak:
        answer = max(answer, isBreakCnt(eggs))
        return
    
    for i in range(N):
        if i == index or eggs[i][0] <= 0:
            continue
        
        eggs[i][0] -= eggs[index][1]
        eggs[index][0] -= eggs[i][1]
        
        eggBreak(index+1)
        
        eggs[i][0] += eggs[index][1]
        eggs[index][0] += eggs[i][1]
    
eggBreak(0)
print(answer)

