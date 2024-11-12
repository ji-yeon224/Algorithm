import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numList = list(map(int, input().split()))

if N <= K:
    print(N)
else:
    counts = [0]*(max(numList)+1)
    maxLen = 0
    left = 0
    right = 1
    counts[numList[left]] += 1
    while left<right and right < N:
        if counts[numList[right]] < K:
            counts[numList[right]]+=1
            right += 1
            maxLen = max(maxLen, right-left)
        else:
            counts[numList[left]] -= 1
            left += 1
            if right < N and left >= right:
                right += 1
    print(maxLen)