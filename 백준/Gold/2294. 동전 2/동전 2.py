N, K = map(int, input().split())

dp = [100001]*100001
coinList = []
for _ in range(N):
    value = int(input())
    coinList.append(value)

for coin in coinList:
    dp[coin] = 1
    for i in range(coin+1, K+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)
        
if dp[K] == 100001:
    print(-1)
else:
    print(dp[K])