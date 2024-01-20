import sys

N = int(sys.stdin.readline())

minDP = []
maxDP = []

arr = list(int(n) for n in sys.stdin.readline().split())
minDP = arr
maxDP = arr


for i in range(1, N):
    arr = list(int(n) for n in sys.stdin.readline().split())
    min1 = arr[0] + min(minDP[0], minDP[1])
    min2 = arr[1] + min(minDP[0], minDP[1], minDP[2])
    min3 = arr[2] + min(minDP[1], minDP[2])
    minDP = [min1, min2, min3]

    max1 = arr[0] + max(maxDP[0], maxDP[1])
    max2 = arr[1] + max(maxDP[0], maxDP[1], maxDP[2])
    max3 = arr[2] + max(maxDP[1], maxDP[2])
    maxDP = [max1, max2, max3]
        
print(max(maxDP), min(minDP))