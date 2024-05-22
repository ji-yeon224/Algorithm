import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
answer = INF
for i in range(3):
    dp = [[-1]*3 for _ in range(N)]
    dp[0] = [INF, INF, INF]
    
    dp[0][i] = graph[0][i]
    for j in range(1, N):
        dp[j][0] = graph[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = graph[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = graph[j][2] + min(dp[j-1][0], dp[j-1][1])
    dp[N-1][i] = INF
    answer = min(answer, min(dp[-1]))
print(answer)