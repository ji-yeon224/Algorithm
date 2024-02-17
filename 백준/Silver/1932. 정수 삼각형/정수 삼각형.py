import sys

N = int(sys.stdin.readline())

dp = [[0] * N for _ in range(N)]

dp[0][0] = int(sys.stdin.readline())

for i in range(1, N):
    input = [int(n) for n in sys.stdin.readline().split()]
    for j in range(len(input)):
        if j == 0:
            dp[i][j] = dp[i-1][j] + input[j]
        elif j == len(input)-1:
            dp[i][j] = dp[i-1][j-1] + input[j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + input[j]
            
print(max(dp[-1]))    