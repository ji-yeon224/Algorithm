N = int(input())

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
graph = [[0]*101 for _ in range(101)] 
for _ in range(N):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1
    move = [d]
    for _ in range(g):
        for i in range(len(move)-1, -1, -1):
            move.append((move[i] + 1) % 4)
    for d in move:
        x = x + dirs[d][1]
        y = y + dirs[d][0]
        
        if 0 <= x < 101 and 0 <= y < 101:
            graph[y][x] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j] == 1 and graph[i+1][j+1] == 1:
            answer += 1
print(answer)