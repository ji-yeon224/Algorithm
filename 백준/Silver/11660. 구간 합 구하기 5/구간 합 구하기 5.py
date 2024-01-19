import sys

N, M = map(int, sys.stdin.readline().split())

dp = []
for _ in range(N):
    dp.append(list(int(n) for n in sys.stdin.readline().split()))

for r in range(N):
    for c in range(N):
        if r > 0 :
            dp[r][c] += dp[r-1][c]
        if c > 0:
            dp[r][c] += dp[r][c-1] 
        if r > 0 and c > 0 :
            dp[r][c] -= dp[r-1][c-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    result = dp[x2][y2]
    if x1 > 0:
        result -= dp[x1-1][y2]
    if y1 > 0:
        result -= dp[x2][y1-1]
    if x1 > 0 and y1 > 0:
        result += dp[x1-1][y1-1]
    print(result)


