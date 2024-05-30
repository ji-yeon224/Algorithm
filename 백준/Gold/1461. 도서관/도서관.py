N, M = map(int, input().split())
numList = list(map(int, input().split()))
plus = []
minus = []
maxDist = 0
for n in numList:
    maxDist = max(maxDist, abs(n))
    if n < 0:
        minus.append(n)
    else:
        plus.append(n)
minus.sort()
plus.sort(reverse = True)

total = 0
for i in range(0, len(plus), M):
    total += plus[i]
    
for i in range(0, len(minus), M):
    total += abs(minus[i])
    
total *= 2
total -= maxDist
print(total)