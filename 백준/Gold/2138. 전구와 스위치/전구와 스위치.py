N = int(input())
curBulb = list(map(int, input()))
destBulb = list(map(int, input()))
answer = int(1e9)

def change(bulb):
    global N
    count = 0
    for i in range(1, N):
        if bulb[i-1] == destBulb[i-1]:
            continue
        count += 1
        bulb[i-1] = 1 - bulb[i-1]
        bulb[i] = 1 - bulb[i]
        if i < N-1:
            bulb[i+1] = 1 - bulb[i+1]
    if bulb == destBulb:
        return count
    else:
        return 1e9

copyBulb = curBulb[:]
answer = change(copyBulb)
copyBulb = curBulb[:]
copyBulb[0] = 1 - copyBulb[0]
copyBulb[1] = 1 - copyBulb[1]

minCount = min(answer, change(copyBulb)+1)
if minCount == 1e9:
    print(-1)
else:
    print(minCount)