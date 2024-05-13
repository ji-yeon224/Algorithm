import sys
input = sys.stdin.readline
N = int(input())
numList = list(map(int, input().split()))
numList.sort()

answer = 0
for i in range(N-2):
    left = i+1
    right = N-1
    goal = -numList[i]
    rIdx = N
    while left < right:
        tmp = numList[left] + numList[right]
        if tmp == goal:
            if numList[left] == numList[right]:
                answer += right - left
            else:
                if rIdx > right:
                    rIdx = right
                    while rIdx >= left and numList[rIdx -1] == numList[right]:
                        rIdx -= 1
                answer += (right - rIdx+1)
            left += 1
        elif tmp < goal:
            left += 1
        else:
            right -= 1
print(answer)