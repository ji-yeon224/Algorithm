import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

T = int(input())


def dfs(cur):
    global result
    visited[cur] = True
    team.append(cur)
    
    nxt = students[cur]
    if visited[nxt]:
        if nxt in team:
            result += (len(team) - team.index(nxt))
        return
    else:
        dfs(nxt)


for _ in range(T):
    N = int(input())
    students = [0] + list(n for n in map(int, input().split()))
    visited = [False] * (N+1)
    result = 0
    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)
    print(N-result)