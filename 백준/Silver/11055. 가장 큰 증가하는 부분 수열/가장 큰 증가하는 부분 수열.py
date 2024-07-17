N = int(input())
numList = [i for i in map(int, input().split())]
dp = [0]*N
dp[0] = numList[0]
for i in range(1, N):
    maxNum = 0
    idx = 0
    for j in range(i):
        if numList[i] > numList[j]:
            dp[i] = max(dp[i], numList[i]+dp[j])
        else:
            dp[i] = max(dp[i], numList[i])
            
print(max(dp))