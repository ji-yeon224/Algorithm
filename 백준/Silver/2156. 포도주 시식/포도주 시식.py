
import sys

N = int(sys.stdin.readline())
wine = []
wine.append(0)
for _ in range(N):
    wine.append(int(sys.stdin.readline()))

dp = [0] * (N+1)
dp[0] = 0
dp[1] = wine[1]
if N >= 2:
    dp[2] = wine[1]+wine[2]

    for i in range(3, N+1):
        dp[i] = max(wine[i-1]+wine[i]+dp[i-3], dp[i-2] + wine[i], dp[i-1])


print(max(dp))