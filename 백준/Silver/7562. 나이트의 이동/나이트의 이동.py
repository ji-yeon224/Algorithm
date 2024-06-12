from collections import deque

T = int(input())

dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
def solution():
    I = int(input())
    curR, curC = map(int, input().split())
    destR, destC = map(int, input().split())
    visited = [[False]*I for _ in range(I)]
    
    queue = deque([])
    queue.append((curR, curC, 0))
    
    visited[curR][curC] = True
    answer = 0
    while queue:
        cr, cc, count = queue.popleft()
        if cr == destR and cc == destC:
            answer = count
            break
        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < I and 0 <= nc < I and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, count+1))
    return answer

for _ in range(T):
    print(solution())