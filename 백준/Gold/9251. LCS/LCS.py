import sys
str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())

str1Len = len(str1)
str2Len = len(str2)
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for i in range(1, str2Len + 1):
    for j in range(1, str1Len + 1):
        if str2[i-1] == str1[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[-1][-1])