import sys

cnt, partyCnt = map(int, sys.stdin.readline().strip().split())

trueMan = set(int(n) for n in sys.stdin.readline().strip().split()[1:])

party = []
for _ in range(partyCnt):
    input = set(int(n) for n in sys.stdin.readline().strip().split()[1:])
    party.append(input)


for _ in range(partyCnt):
    for p in party:
        if trueMan.intersection(p):
            trueMan = p.union(trueMan)

result = 0
for p in party:
    if p & trueMan:
        continue
    result += 1

print(result)