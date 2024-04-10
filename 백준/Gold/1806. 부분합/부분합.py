import sys
input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().split())
numList = [n for n in map(int, input().split())]

p1 = 0
p2 = 0
curSum = numList[0]
cnt = INF

while p1 < N and p2 < N:
    if curSum >= M:
        cnt = min(cnt, p2-p1+1)
        curSum -= numList[p1]
        p1 += 1
    else:
        p2 += 1
        if p2 < N:
            curSum += numList[p2]
        
print(cnt if cnt != INF else 0)