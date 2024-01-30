import sys

N = int(sys.stdin.readline())
arr = [int(num) for num in sys.stdin.readline().split()]

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

maxLen = max(dp)
print(maxLen)
result = []
for i in range(len(dp)-1, -1, -1):
    if dp[i] == maxLen:
        result.insert(0, arr[i])
        maxLen -= 1


for num in result:
    print(num, " ")