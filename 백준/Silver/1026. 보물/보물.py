N = int(input())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

answer = 0
for _ in range(N):
    answer += (min(aList) * max(bList))
    aList.pop(aList.index(min(aList)))
    bList.pop(bList.index(max(bList)))
print(answer)