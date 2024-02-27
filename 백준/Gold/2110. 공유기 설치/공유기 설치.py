import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

left = 1
right = house[-1]
answer = 0

def binarySearch(left, right):
    global answer
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        prev = house[0]
        for i in range(1, N):
            if house[i] - prev >= mid:
                prev = house[i]
                cnt += 1
            if cnt > C:
                break
        
        if cnt >= C:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
        

if N == 2:
    print(house[1] - house[0])
else:
    binarySearch(left, right)
    print(answer)