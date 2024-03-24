import sys
input = sys.stdin.readline

N = int(input())
numList = [n for n in map(int, input().split())]

plus, minus, mult, divied = map(int, input().split())

minValue = int(1e9)
maxValue = -int(1e9)

def dfs(i, value):
    global plus, minus, mult, divied, maxValue, minValue
    
    if i == N:
        minValue = min(minValue, value)
        maxValue = max(maxValue, value)
        return
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, value + numList[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, value - numList[i])
            minus += 1
        if mult > 0:
            mult -= 1
            dfs(i+1, value * numList[i])
            mult += 1
        if divied > 0:
            divied -= 1
            dfs(i+1, int(value / numList[i]))
            divied += 1
            
dfs(1, numList[0]) 

print(maxValue)
print(minValue)