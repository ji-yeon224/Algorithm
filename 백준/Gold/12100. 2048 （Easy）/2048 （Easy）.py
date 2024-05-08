import copy


def moveUp(tmpboard):
    global N
    for c in range(N):
        index = 0
        for r in range(1, N):
            if tmpboard[r][c] != 0:
                num = tmpboard[r][c]
                tmpboard[r][c] = 0
                if tmpboard[index][c] == 0:
                    tmpboard[index][c] = num
                elif tmpboard[index][c] == num:
                    tmpboard[index][c] *= 2
                    index += 1
                else:
                    index += 1
                    tmpboard[index][c] = num
    return tmpboard

def moveDown(tmpboard):
    global N
    for c in range(N):
        index = N-1
        for r in range(N-2, -1, -1):
            if tmpboard[r][c] != 0:
                num = tmpboard[r][c]
                tmpboard[r][c] = 0
                
                if tmpboard[index][c] == 0:
                    tmpboard[index][c] = num
                elif tmpboard[index][c] == num:
                    tmpboard[index][c] *= 2
                    index -= 1
                else:
                    index -= 1
                    tmpboard[index][c] = num
            
    return tmpboard
                
def moveRight(tmpboard):
    global N
    for r in range(N):
        index = N-1
        for c in range(N-2, -1, -1):
            if tmpboard[r][c] != 0:
                num = tmpboard[r][c]
                tmpboard[r][c] = 0
                
                if tmpboard[r][index] == 0:
                    tmpboard[r][index] = num
                elif tmpboard[r][index] == num:
                    tmpboard[r][index] *= 2
                    index -= 1
                else:
                    index -= 1
                    tmpboard[r][index] = num
    return tmpboard
    
def moveLeft(tmpboard):
    global N
    for r in range(N):
        index = 0
        for c in range(1, N):
            if tmpboard[r][c] != 0:
                num = tmpboard[r][c]
                tmpboard[r][c] = 0
                
                if tmpboard[r][index] == 0:
                    tmpboard[r][index] = num
                elif tmpboard[r][index] == num:
                    tmpboard[r][index] *= 2
                    index += 1
                else:
                    index+=1
                    tmpboard[r][index] = num
            
        
    return tmpboard

def dfs(count, moveBoard):
    global maxBlock
    if count == 5:
        for b in moveBoard:
            maxBlock = max(maxBlock, max(b))
        return
    for i in range(4):
        if i == 0:
            move = moveUp(copy.deepcopy(moveBoard))
            dfs(count+1, move)
        elif i == 1:
            move = moveDown(copy.deepcopy(moveBoard))
            dfs(count+1, move)
        elif i == 2:
            move = moveLeft(copy.deepcopy(moveBoard))
            dfs(count+1, move)
        elif i == 3:
            move = moveRight(copy.deepcopy(moveBoard))
            dfs(count+1, move)

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
maxBlock = 0
for b in board:
    maxBlock = max(maxBlock, max(b))

dfs(0, board)
print(maxBlock)    

