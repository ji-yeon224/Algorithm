import sys

graph = [[n for n in map(int, sys.stdin.readline().split())] for _ in range(9)]

empty = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))
            
def column(r, n):
    for i in range(9):
        if graph[r][i] == n:
            return False
    return True

def row(c, n):
    for i in range(9):
        if graph[i][c] == n:
            return False
    return True
    
def square(r, c, n):
    for i in range(3):
        for j in range(3):
            if graph[r//3*3+i][c//3*3+j] == n:
                return False
    return True
    
def sudoku(cnt):
    
    if cnt >= len(empty):
        for i in range(9):
            print(" ".join(map(str, graph[i])))
        exit()
    
    
    curR, curC = empty[cnt]
    for i in range(1, 10):
        if column(curR, i) and row(curC, i) and square(curR, curC, i):
            graph[curR][curC] = i
            sudoku(cnt+1)
            graph[curR][curC] = 0
    



sudoku(0)
