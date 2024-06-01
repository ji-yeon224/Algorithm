N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

count = 0
coin = K
for c in coins[::-1]:
    count += coin // c
    coin %= c
print(count)