import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
airplanes = [int(input()) for _ in range(P)]
gateList = [i for i in range(G+1)]

def findRoot(gateNum):
    if gateList[gateNum] == gateNum:
        return gateNum
    else:
        gateList[gateNum] = findRoot(gateList[gateNum])
        return gateList[gateNum]
def union(a):
    b = findRoot(a-1)
    gateList[a] = b

answer = 0
for airplane in airplanes:
    gate = findRoot(airplane)
    if gate == 0:
        break
    answer += 1
    union(gate)

print(answer)