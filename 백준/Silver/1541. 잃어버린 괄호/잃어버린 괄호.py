import sys
input = sys.stdin.readline

expression = input().strip()
minusExp = expression.split('-')
result = 0

for i, m in enumerate(minusExp):
    curNum = 0
    if '+' in m:
        plusExp = m.split('+')
        for p in plusExp:
            curNum += int(p)
    else:
        curNum = int(m)
    
    if i == 0:
        result += curNum
    else:
        result -= curNum

print(result)