import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

INF = int(1e9)

visited = [INF] * 100001


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    
    while heap:
        time, cur = heapq.heappop(heap)
        if visited[cur] < time:
            continue
        for t, next in [(time, cur*2), (time+1, cur+1), (time+1, cur-1)]:
            if next > -1 and next <= 100000 and t < visited[next]:
                heapq.heappush(heap, (t, next))
                visited[next] = t



dijkstra(N)
print(visited[K])

# visited = [-1] * 100001

# def bfs(n, k):
#     queue = deque([n])
#     visited[n] = 0
#     while queue:
#         cur = queue.popleft()
#         if cur == k:
#             print(visited[cur])
#             break
        
#         if cur*2 <= 100000 and visited[cur*2] == -1:
#             queue.appendleft(cur*2)
#             visited[cur*2] = visited[cur]
        
#         for move in (cur - 1, cur + 1):
#             if move > -1 and move <= 100000 and visited[move] == -1:
#                 queue.append(move)
#                 visited[move] = visited[cur]+1



# bfs(N, K)
