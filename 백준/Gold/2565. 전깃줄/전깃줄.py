import sys
N = int(sys.stdin.readline())
dict = {}
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    dict[a] = b
    
sortKeys = sorted(list(dict.keys()))
dp = [1] * N

for i in range(1, N):
    curA = sortKeys[i]
    curB = dict[curA]
    for j in range(i):
        if dict[sortKeys[j]] < curB:
            dp[i] = max(dp[j]+1, dp[i])

print(N-max(dp))