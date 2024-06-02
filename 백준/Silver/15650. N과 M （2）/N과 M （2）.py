N, M = map(int, input().split())

def backtracking(start, depth, nums):
    global N, M
    if depth == M:
        print(' '.join(map(str, nums)))
        return
    for i in range(start+1, N+1):
        newList = nums + [i]
        backtracking(i, depth+1, newList)
for i in range(1, N+1):
    backtracking(i, 1, [i])