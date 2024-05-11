
N = int(input())
dp = [N]*(N+1)
numList = [0]*(N+1)
dp[1] = 0
for i in range(2, N+1):
    
    minCnt = dp[i]
    useNum = i
    if i % 2 == 0 and dp[i//2]+1 < minCnt:
        minCnt = dp[i//2]+1
        useNum = i//2   
    if i % 3 == 0 and dp[i//3]+1 < minCnt:
        minCnt = dp[i//3]+1
        useNum = i//3
    if dp[i-1]+1 < minCnt:
        minCnt = dp[i-1]+1
        useNum = i-1
    dp[i] = minCnt
    numList[i] = useNum

print(dp[N])
num = N
while num != 0:
    print(num, end = ' ')
    num = numList[num]