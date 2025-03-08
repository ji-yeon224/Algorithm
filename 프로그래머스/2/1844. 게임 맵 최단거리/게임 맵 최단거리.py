from collections import deque

def bfs(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True    
    
    queue = deque([(0, 0, 1)])
    while queue:
        curR, curC, move = queue.popleft()
        if curR == n-1 and curC == m-1:
            answer = move
            break
        for dr, dc in dir:
            nr = dr + curR
            nc = dc + curC
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, move+1))
        
    return answer
    
def solution(maps):
    answer = bfs(maps)
    
    return answer