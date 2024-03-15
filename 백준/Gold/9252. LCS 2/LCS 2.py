
import sys
input = sys.stdin.readline


str1 = ['0'] + list(input().rstrip())
str2 = ['0'] + list(input().rstrip())
len1 = len(str1)
len2 = len(str2)

dp = [['' for _ in range(len1)] for _ in range(len2)]

for i in range(1, len2):
    for j in range(1, len1):
        if str1[j] == str2[i]:
            dp[i][j] = dp[i-1][j-1] + str1[j]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

result = dp[-1][-1]
print(len(result))
if len(result) != 0:
    print(result)
        