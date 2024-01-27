import sys


N = int(sys.stdin.readline())
result = []
for _ in range(N):
    result.append([int(n) for n in sys.stdin.readline().split()])

for i in range(1, N):
    result[i][0] += min(result[i-1][1], result[i-1][2])
    result[i][1] += min(result[i-1][0], result[i-1][2])
    result[i][2] += min(result[i-1][1], result[i-1][0]) 

print(min(result[N-1]))