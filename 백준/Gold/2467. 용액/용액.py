import sys
input = sys.stdin.readline

N = int(input())
numList = [n for n in map(int, input().split())]


minNum = numList[0] + numList[N-1]
result = (numList[0], numList[N-1])
left = 0
right = N-1
while left < right:
    leftNum = numList[left]
    rightNum = numList[right]
    mix = leftNum + rightNum
    
    if abs(minNum) > abs(mix):
        result = (leftNum, rightNum)
        minNum = mix
        
    if mix == 0:
        minNum = 0
        break
    elif mix < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
