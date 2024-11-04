import sys
input = sys.stdin.readline

T = int(input())
expressions = []

def dfs(exp, index, N):
    if index == N+1:
        result = eval(exp.replace(' ', ''))
        if result == 0:
            expressions.append(exp)
        return
    dfs(exp+' '+str(index), index+1, N)
    dfs(exp+"+"+str(index), index+1, N)
    dfs(exp+"-"+str(index), index+1, N)

for _ in range(T):
    N = int(input())
    dfs("1", 2, N)
    print(*expressions, sep="\n")
    print()
    expressions = []