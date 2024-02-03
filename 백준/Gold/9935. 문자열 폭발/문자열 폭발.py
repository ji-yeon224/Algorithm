import sys

full = [c for c in sys.stdin.readline().strip()]
bomb = [c for c in sys.stdin.readline().strip()]
last = bomb[-1]
bombLen = len(bomb)

stack = []

for c in full:
    stack.append(c)
    if c == last:
        if stack[-bombLen:] == bomb:
            for _ in range(bombLen):
                stack.pop()

if not stack:
    print("FRULA")
else: 
    print("".join(stack))