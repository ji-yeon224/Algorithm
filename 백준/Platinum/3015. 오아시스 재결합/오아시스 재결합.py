import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 0
for _ in range(N):
    height = int(input())
    while stack and stack[-1][0] < height:
        count += stack.pop()[1]
    if not stack:
        stack.append((height, 1))
        continue
    if stack[-1][0] == height:
        cnt = stack.pop()[1]
        if stack: count += 1
        count += cnt
        stack.append((height, cnt+1))
    else:
        stack.append((height, 1))
        count += 1
print(count)
