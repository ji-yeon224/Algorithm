import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
graph.sort(key = lambda x : (x[0], -x[1]) )

total = graph[0][1] - graph[0][0]
end = graph[0][1]
for i in range(1, N):
    nxt = graph[i]
    nxtStart = nxt[0]
    nxtEnd = nxt[1]
    if nxtEnd <= end:
        continue
    
    if nxtStart > end:
        total += (nxtEnd - nxtStart)
        end = nxtEnd
    else:
        total += (nxtEnd - end)
        end = nxtEnd
print(total)