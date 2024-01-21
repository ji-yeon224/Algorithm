import sys
n = int(sys.stdin.readline())
arr = list(int(num) for num in sys.stdin.readline().strip().split())
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))