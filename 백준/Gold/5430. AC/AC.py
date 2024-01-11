from collections import deque

n = int(input())

def solution():
    command = input()
    nCnt = int(input())
    arr = deque(input()[1:-1].split(","), maxlen = nCnt)

    reverseCnt = 0

    for c in command:
        prevCmd = c
        if c == "R":
            reverseCnt += 1
        elif c == "D":
            if len(arr) > 0:
                if reverseCnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                return "error"
            
    if reverseCnt % 2 == 1:
        arr.reverse()
    return "["+",".join(arr)+"]"

for _ in range(n):
    print(solution())
