from collections import defaultdict, deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    lights[1][1] = True
    queue = deque([(1, 1)])
    while queue:
        cur = queue.popleft()
        visited[cur[0]][cur[1]] = True
        if cur in switches:
            for sr, sc in switches[cur]:
                if visited[sr][sc]:
                    continue
                lights[sr][sc] = True
                for dr, dc in dirs:
                    nr = sr + dr
                    nc = sc + dc
                    if 0 < nr <= N and 0 < nc <= N and visited[nr][nc]:
                        queue.append((sr, sc))
                        break
        for dr, dc in dirs:
            nr = cur[0] + dr
            nc = cur[1] + dc
            if 0 < nr <= N and 0 < nc <= N and not visited[nr][nc] and lights[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
               
N, M = map(int, input().split())
switches = defaultdict(list)
visited = [[False]*(N+1) for _ in range(N+1)]
lights = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x, y, a, b = map(int, input().split())
    switches[(x, y)].append((a, b))

bfs()
answer = 0
for light in lights:
    answer += light.count(True)
print(answer)