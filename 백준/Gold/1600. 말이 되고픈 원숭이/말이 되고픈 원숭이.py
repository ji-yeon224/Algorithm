from collections import deque

def bfs():
    global K, W, H
    visited = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]
    queue = deque([])
    queue.append((0, 0, 0))
    visited[0][0][0] = 0
    answer = -1
    while queue:
        r, c, k = queue.popleft()
        if r == H-1 and c == W-1:
            answer = visited[r][c][k]
            break
        if k < K:
            for dr, dc in horseDir:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == 0 and visited[nr][nc][k+1] < 0:
                    visited[nr][nc][k+1] = visited[r][c][k] + 1
                    queue.append((nr, nc, k+1))
        for dr, dc in closeDir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == 0 and visited[nr][nc][k] < 0:
                visited[nr][nc][k] = visited[r][c][k] + 1
                queue.append((nr, nc, k))
    return answer


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

closeDir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
horseDir = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
print(bfs())