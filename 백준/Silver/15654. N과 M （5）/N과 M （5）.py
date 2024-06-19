N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

def backtracking(visited, depth, answer):
    global N, M
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            newAnswer = answer + [numList[i]]
            backtracking(visited, depth+1, newAnswer)
            visited[i] = False

visited = [False]*N
for i in range(N):
    visited[i] = True
    backtracking(visited, 1, [numList[i]])
    visited[i] = False