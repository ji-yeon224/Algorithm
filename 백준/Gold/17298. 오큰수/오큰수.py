N = int(input())
numList = list(map(int, input().split()))
stack = []
answer = [-1] * N
for i in range(N-1, -1, -1):
    curNum = numList[i]
    if not stack:
        stack.append(curNum)
        continue
    while stack:
        if stack[-1] > curNum:
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(curNum)   


print(' '.join(map(str, answer)))