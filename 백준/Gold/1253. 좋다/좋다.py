import sys
input = sys.stdin.readline

N = int(input())
numArr = list(map(int, input().split()))
numArr.sort()
total = 0
if N < 3:
    print(0)
else:
    for i in range(N):
        tmp = numArr[:i] + numArr[i+1:]
        left, right = 0, len(tmp)-1
        dest = numArr[i]
        while left < right:
            tmpSum = tmp[left]+tmp[right]
            if tmpSum == dest:
                total += 1
                break
            if tmpSum < dest:
                left += 1
                continue
            if tmpSum > dest:
                right -= 1
                continue
    print(total)