N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)

for day in range(N-1, -1, -1):
    time, profit = works[day]
    if N - day < time:
        dp[day] = dp[day+1]
        continue
    dp[day] = max(dp[day+1], profit + dp[time+day])
print(dp[0])