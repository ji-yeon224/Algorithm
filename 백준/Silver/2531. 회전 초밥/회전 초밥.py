import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(N)]

maxCnt = 0
left = 0
right = k
for i in range(N):
    left = i
    right = (i+k)%N
    if left < right:
        eat = set(dishes[left: right])
    else:
        eat = set(dishes[left:])
        eat.update(dishes[:right])
    eat.add(c)
    maxCnt = max(maxCnt, len(eat))
print(maxCnt)