import sys

N, M = map(int, sys.stdin.readline().split())
house = []
chicken = []

for i in range(N):
    input = [int(n) for n in sys.stdin.readline().split()]
    for j in range(N):
        if input[j] == 1:
            house.append((i, j))
        elif input[j] == 2:
            chicken.append((i, j))

answer = int(1e9)
visited = [False] * len(chicken)
def dfs(cidx, cnt):
    global answer
    distSum = 0
    if cnt == M:

        for h in house:
            dist = int(1e9)
            for i, c in enumerate(chicken):
                if visited[i]:
                    tmp = abs(h[0]-c[0]) + abs(h[1]-c[1])
                    dist = min(dist, tmp)
            distSum += dist
        answer = min(answer, distSum)

        return

    for i in range(cidx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False
    
dfs(0, 0)
print(answer)