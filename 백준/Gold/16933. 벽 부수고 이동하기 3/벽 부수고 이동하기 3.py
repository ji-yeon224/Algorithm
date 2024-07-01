from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0  # 시작 지점의 방문 표시
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    queue = deque([(0, 0, 0, 1)])  # (row, col, 벽 부순 횟수, 거리)
    
    while queue:
        r, c, k, dist = queue.popleft()
        
        if r == N-1 and c == M-1:
            print(dist)
            return
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0 and (visited[nr][nc] == -1 or visited[nr][nc] > k):
                    visited[nr][nc] = k
                    queue.append((nr, nc, k, dist+1))
                elif graph[nr][nc] == 1 and k < K and (visited[nr][nc] == -1 or visited[nr][nc] > k + 1):
                    if dist % 2 == 1:  # 낮일 때
                        visited[nr][nc] = k + 1
                        queue.append((nr, nc, k + 1, dist+1))
                    else:  # 밤일 때
                        queue.append((r, c, k, dist+1))
    
    print(-1)

bfs()
