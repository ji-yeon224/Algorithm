N, M = map(int, input().split())
numList = [n for n in map(int, input().split())]

left = 0
right = 1
count = 0

while left <= N and right <= N:
    sumList = numList[left:right]
    total = sum(sumList)
    if total == M:          
        count += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
print(count)