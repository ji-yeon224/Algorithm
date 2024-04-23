import sys

input = sys.stdin.readline
N = int(input())
graph = [int(input()) for _ in range(N)] 

stack = [graph[0]]
answer = 0

for i in range(1, N):
    if graph[i] < stack[-1]:
        stack.append(graph[i])
        answer += (len(stack)-1)
    else:
        while stack:
            if stack[-1] > graph[i]:
                break
            stack.pop()
        stack.append(graph[i])
        answer += (len(stack)-1)
print(answer)