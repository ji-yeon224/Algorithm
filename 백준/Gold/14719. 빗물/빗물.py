H, W = map(int, input().split())
graph = list(map(int, input().split()))
answer = 0
for i in range(1, W-1):
    leftMax = max(graph[:i])
    rightMax = max(graph[i+1:])
    minHeight = min(leftMax, rightMax)
    if minHeight > graph[i]:
        answer += minHeight-graph[i]
    
print(answer)