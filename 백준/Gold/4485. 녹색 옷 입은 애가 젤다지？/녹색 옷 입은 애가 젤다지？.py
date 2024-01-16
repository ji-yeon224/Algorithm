from collections import deque
import sys


def solution(cnt, idx) :
    global visited
    global cost

    queue = deque([(0, 0)])
    map = []
    dir: [(int, int)] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cost = []

    visited = [[False for j in range(cnt)] for i in range(cnt)]
    cost = [[sys.maxsize]*cnt for _ in range(cnt)]
    for _ in range(cnt):
        map.append([int(i) for i in sys.stdin.readline().strip().split()])
    cost[0][0] = map[0][0]

    while queue:
       cur = queue.popleft()
       for d in dir:
        nxtR = cur[0] + d[0]
        nxtC = cur[1] + d[1]
        if nxtR >= 0 and nxtR < cnt and nxtC >= 0 and nxtC < cnt:
            c = map[nxtR][nxtC] + cost[cur[0]][cur[1]]
            if cost[nxtR][nxtC] > c:
                cost[nxtR][nxtC] = c
                queue.append([nxtR, nxtC])
    print(f'Problem {idx}: {cost[cnt-1][cnt-1]}')

idx = 1
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    else:
        solution(cnt = n, idx = idx)
        idx += 1