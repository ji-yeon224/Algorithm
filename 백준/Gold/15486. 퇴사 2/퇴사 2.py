import sys
input = sys.stdin.readline
N = int(input())
works = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0]*(N+2)

for i in range(N-1, -1, -1):
    t, p = works[i]
    if i+t > N:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(dp[i+1], dp[i+t]+p)
print(dp[0])