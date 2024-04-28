N = int(input())
top = list(map(int, input().split()))

stack = []
stack.append(0)
print(0, end = " ")
for i in range(1, N):
    
    if top[stack[-1]] < top[i]:
        while stack and top[stack[-1]] <= top[i]:
            stack.pop()
    
    if not stack:
        print(0, end = ' ')
    else: print(stack[-1]+1, end = ' ')
    stack.append(i)