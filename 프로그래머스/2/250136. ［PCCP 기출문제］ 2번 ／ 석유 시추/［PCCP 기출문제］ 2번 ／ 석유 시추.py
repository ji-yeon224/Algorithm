from collections import deque

visited = []
injectList = {}

def bfs(r, c, N, M, land):
    global visited, injectList
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    colList = set([c])
    visited[r][c] = True
    count = 1
    queue = deque([(r, c)])
    while queue:
        curR, curC = queue.popleft()
        for dr, dc in dirs:
            nr = curR+dr
            nc = curC+dc
            if 0 <= nr < N and 0 <= nc < M and land[nr][nc]==1 and not visited[nr][nc]:
                colList.add(nc)
                visited[nr][nc] = True
                queue.append((nr, nc))
                count += 1
    for c in colList:
        injectList[c] += count
def solution(land):
    global visited, injectList
    
    N = len(land)
    M = len(land[0])
    injectList = {i: 0 for i in range(M)}
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, N, M, land)
                
    
    return max(injectList.values())