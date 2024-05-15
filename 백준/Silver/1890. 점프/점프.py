N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        dist = board[i][j]
        if dp[i][j] == 0 or dist == 0:
            continue
        if i+dist < N:
            dp[i+dist][j] += dp[i][j]
        if j + dist < N:
            dp[i][j+dist] += dp[i][j]
print(dp[-1][-1])