N, M = map(int, input().split())

def makeList(depth, nums):
    global N, M
    if depth == M:
        print(' '.join(map(str, nums)))
        return
    for i in range(1, N+1):
        nxtNums = nums + [i]
        makeList(depth+1, nxtNums)
for i in range(1, N+1):
    makeList(1, [i])