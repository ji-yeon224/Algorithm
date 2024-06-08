from collections import deque

n = int(input())
stack = deque([1])
numList = []
nowNum = 1
operator = []
flag = True
for _ in range(n):
    num = int(input())
    while nowNum <= num:
        stack.append(nowNum)
        nowNum += 1
        operator.append("+")
    if stack[-1] == num:
        stack.pop()
        operator.append("-")
    else:
        flag = False
        break
    
if not flag:
    print("NO")
else:
    for o in operator:
        print(o)