import sys
input = sys.stdin.readline

N = int(input())
research = [n for n in map(int, input().split())]

research.sort()

left = 0
right = N-1
minVal = abs(research[left] + research[right])
result = [research[left], research[right]]

while left<right:
    newData = research[left] + research[right]
    if minVal > abs(newData):
        minVal = abs(newData)
        result[0] = research[left]
        result[1] = research[right]
    
    if newData == 0:
        break
    elif newData < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])