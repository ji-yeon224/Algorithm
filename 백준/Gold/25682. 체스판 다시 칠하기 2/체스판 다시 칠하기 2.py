
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
chess = [list(input().rstrip()) for _ in range(N)]

bSum = [[0]*(M+1) for _ in range(N+1)]
wSum = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            if chess[i][j] == 'B':
                bSum[i][j] = bSum[i][j-1] + bSum[i-1][j] - bSum[i-1][j-1]
                wSum[i][j] = wSum[i][j-1] + wSum[i-1][j] - wSum[i-1][j-1] + 1
            else:
                bSum[i][j] = bSum[i][j-1] + bSum[i-1][j] - bSum[i-1][j-1] + 1
                wSum[i][j] = wSum[i][j-1] + wSum[i-1][j] - wSum[i-1][j-1]
        else:
            if chess[i][j] == 'B':
                bSum[i][j] = bSum[i][j-1] + bSum[i-1][j] - bSum[i-1][j-1] + 1
                wSum[i][j] = wSum[i][j-1] + wSum[i-1][j] - wSum[i-1][j-1]
            else:
                bSum[i][j] = bSum[i][j-1] + bSum[i-1][j] - bSum[i-1][j-1]
                wSum[i][j] = wSum[i][j-1] + wSum[i-1][j] - wSum[i-1][j-1] + 1

result = int(1e9) 
for i in range(N-K+1):
    for j in range(M-K+1):
        bRes = bSum[i+K-1][j+K-1] - bSum[i-1][j+K-1] - bSum[i+K-1][j-1] + bSum[i-1][j-1]
        wRes = wSum[i+K-1][j+K-1] - wSum[i-1][j+K-1] - wSum[i+K-1][j-1] + wSum[i-1][j-1]
        result = min(result, bRes, wRes)


print(result)