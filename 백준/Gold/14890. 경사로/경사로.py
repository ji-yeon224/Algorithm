import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
    
count = 0

def checkRoad(line):
    global L, N
    visited = [False] * N
    for i in range(0, N-1):
        
        if line[i] == line[i+1]:
            continue
        if abs(line[i] - line[i+1]) > 1:
            return False
        elif line[i] < line[i+1]:
            height = line[i]
            for j in range(i, i-L, -1):
                if j < 0 or line[j] != height or visited[j]:
                    return False
                visited[j] == True
                
        elif line[i] > line[i+1]:
            height = line[i+1]
            for j in range(i+1, i+L+1):
                if j >= N or line[j] != height or visited[j]:
                    return False
                visited[j] = True
    return True

for i in range(N):
    if checkRoad(graph[i]):
        count += 1
for i in range(N):
    roads = []
    for j in range(N):
        roads.append(graph[j][i])
    if checkRoad(roads):
        count += 1
print(count)
    