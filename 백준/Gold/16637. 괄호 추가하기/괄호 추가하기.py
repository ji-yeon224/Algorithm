N = int(input())

exp = list(input())
answer = -1*2**31

def calculate(n1, n2, op):
    if op == '*':
        return int(n1)*int(n2)
    elif op == '-':
        return int(n1)-int(n2)
    else:
        return int(n1)+int(n2)

def dfs(index, total):
    global N, answer
    if index == N-1:
        answer = max(answer, total)
        return
    if index+2 < N:
        dfs(index+2, calculate(total, exp[index+2], exp[index+1]))
    if index+4 < N:
        n2 = calculate(exp[index+2], exp[index+4], exp[index+3])
        dfs(index+4, calculate(total, n2, exp[index+1]))
dfs(0, int(exp[0]))
print(answer)