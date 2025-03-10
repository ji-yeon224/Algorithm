import sys
n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n ==2:
    print(3)
else:
    dp = [0, 1, 3]
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2]*2)
    print(dp[n]%10007)