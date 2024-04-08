import sys

input = sys.stdin.readline

N = int(input())
numList = [n for n in map(int, input().split())]
numList.sort()
X = int(input())

leftIdx = 0
rightIdx = N-1
answer = 0

while leftIdx < rightIdx:
    plusNum = numList[leftIdx] + numList[rightIdx]
    if plusNum == X:
        answer += 1
        leftIdx += 1
    elif plusNum < X:
        leftIdx += 1
    else:
        rightIdx -= 1
print(answer)