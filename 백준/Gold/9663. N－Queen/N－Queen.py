N = int(input())

row = [0]*N
answer = 0

def isAttack(cur):
    
    for i in range(cur):
        if row[i] == row[cur] or abs(cur-i) == abs(row[i] - row[cur]):
            return True
    return False

def dfs(cur):
    global answer
    
    if cur == N:
        answer += 1
        return
    
    for i in range(N):
        row[cur] = i
        if not isAttack(cur):
            dfs(cur+1)
    
dfs(0)
print(answer)