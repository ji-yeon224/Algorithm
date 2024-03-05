
import sys

input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().split())
dict = {i: [] for i in range(1, N+1)}

for i in range(M):
    A, B, C = map(int, input().split())
    dict[A].append((B, C))

dist = [INF] * (N+1)

def bellman():
    dist[1] = 0
    
    for t in range(N):
        for i in range(1, N+1):
            for n, d in dict[i]:
                if dist[i] != INF and dist[n] > dist[i]+d:
                    dist[n] = dist[i]+d
                    if t == N-1:
                        print(-1)
                        exit()
                

bellman()
for i in range(2, N+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])