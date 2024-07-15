T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    maxPrice = 0
    for i in range(N-1, -1, -1):
        if maxPrice < price[i]:
            maxPrice = price[i]
        else:
            profit += (maxPrice - price[i])
    print(profit)