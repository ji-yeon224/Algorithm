import sys
from collections import deque

infix = list(sys.stdin.readline().strip())


result = ""
stack = deque()
for s in infix:
    if s == "(":
        stack.append(s)
    elif s == "*" or s == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            result += stack.pop()
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.pop()
    elif s == "+" or s == "-":
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.append(s)
    else: 
        result += s

while stack:
    result += stack.pop()
print(result)
