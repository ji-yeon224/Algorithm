import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))

prices = list(map(int, input().split()))

minPrice = prices[0]
result = dist[0] * prices[0]
for i in range(1, N-1):
    if prices[i] < minPrice:
        minPrice = prices[i]
    result += (minPrice * dist[i])
print(result)