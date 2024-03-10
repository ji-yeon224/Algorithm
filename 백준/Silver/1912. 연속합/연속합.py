import sys
input = sys.stdin.readline
N = int(input())
numArr = [n for n in map(int, input().split())]
dp = [0]*N
dp[0] = numArr[0]
for i in range(1, N):
    if dp[i-1]+numArr[i] <= numArr[i]:
        dp[i] = numArr[i]
    else:
        dp[i] = numArr[i] + dp[i-1]
print(max(dp))
