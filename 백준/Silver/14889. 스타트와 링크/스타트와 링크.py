import sys
input = sys.stdin.readline

N = int(input())
graph = [[n for n in map(int, input().split())] for _ in range(N)]
visited = [False] * N

answer = int(1e9)

def dfs(start, cnt):
    global answer, N
    if cnt == N//2:
        team1 = 0
        team2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        answer = min(answer, abs(team1-team2))
        return
    else:
        for i in range(start, N):
            if not visited[i]:
                visited[i] = True
                dfs(i, cnt + 1)
                visited[i] = False

dfs(0, 0)
print(answer)