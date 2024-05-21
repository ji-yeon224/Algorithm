from collections import deque

N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))

friends = {i: [] for i in range(1, N+1)}
for _ in range(M):
    f1, f2 = map(int, input().split())
    friends[f1].append(f2)
    friends[f2].append(f1)

def bfs(start):
    queue = deque([])
    queue.append(start)
    total = candies[start]
    count = 1
    while queue:
        curNum = queue.popleft()
        for nxt in friends[curNum]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                total += candies[nxt]
                count += 1
    return (count, total)

group = []
visited = [False]*(N+1)
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        count, total = bfs(i)
        group.append((count, total))

dp = [0]*(K+1)
for i in range(len(group)):
    friends, candy = group[i]
    for j in range(K, friends-1, -1):
        dp[j] = max(dp[j-friends]+candy, dp[j])

print(dp[K-1])
