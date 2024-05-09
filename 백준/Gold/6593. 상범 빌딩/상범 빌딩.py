from collections import deque

dirs = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]


def bfs(start):
    global L, R, C
    queue = deque()
    queue.append((start[0], start[1], start[2], 0))
    flag = False
    while queue:
        curL, curR, curC, time = queue.popleft()
        
        if flag:
            break
        
        for dl, dr, dc in dirs:
            nl = curL + dl
            nr = curR + dr
            nc = curC + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and graph[nl][nr][nc] != '#' and not visited[nl][nr][nc]:
                if graph[nl][nr][nc] == 'E':
                    flag = True
                    print("Escaped in %d minute(s)." % (time+1))
                    break
                queue.append((nl, nr, nc, time + 1))
                visited[nl][nr][nc] = True
                
    if not flag:
        print("Trapped!")



while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    graph = []
    S = (0, 0, 0)
    for l in range(L):
        layer = []
        for r in range(R):
            tmp = list(input())
            layer.append(tmp)
            if 'S' in tmp:
                S = (l, r, tmp.index('S'))
                visited[l][r][tmp.index('S')] = True
        
        input()
        graph.append(layer)
    bfs(S)