import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))


left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        if tree < mid:
            continue
        cnt += (tree - mid)
        
        if cnt > M:
            break
    
    if cnt >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)