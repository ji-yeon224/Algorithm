num = int(input())

dp = []
dp.append(0)
dp.append(1)
dp.append(2)

if num > 2:
    for i in range(3, num+1):
        dp.append((dp[i-1] + dp[i-2]) % 10007)
print(dp[num])