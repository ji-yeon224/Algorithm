
import sys
input = sys.stdin.readline

N = int(input())
weight = [n for n in map(int, input().split())]
M = int(input())
ball = [n for n in map(int, input().split())]

dp = [[False] * 15001 for _ in range(N+1)]

def check(cnt, w):
    if cnt > N:
        return
    
    if dp[cnt][w]:
        return
    dp[cnt][w] = True
    check(cnt+1, w+weight[cnt-1])
    check(cnt+1, abs(w-weight[cnt-1]))
    check(cnt+1, w)
    
check(0, 0)


for b in ball:
    if b > 500*N:
        print("N", end=" ")
    elif dp[N][b]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
