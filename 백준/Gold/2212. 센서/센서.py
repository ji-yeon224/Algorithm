import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

if N <= K:
    print(0)
else:
    sensorList = list(map(int, input().split()))
    sensorList.sort()
    dist = []
    for i in range(1, N):
        dist.append(sensorList[i] - sensorList[i-1])
    dist.sort(reverse = True)
    
    for i in range(K-1):
        dist.pop(0)
    
    print(sum(dist))