
from collections import deque

while True:
    string = list(input())
    if len(string) == 1 and string[0] == '.':
        break
    stack = deque([])
    answer = "yes"
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = "no"
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = "no"
                break
    if stack:
        answer = "no"
    print(answer)
