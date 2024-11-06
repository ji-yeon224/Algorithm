import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
move = list(map(int, input().split()))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

castle = [deque() for _ in range(P+1)]
board = []
answer = [0 for _ in range(P+1)]
for i in range(N):
    line = input().rstrip()
    board.append(list(line))
    for j in range(M):
        if line[j] == "." or line[j] == "#":
            continue
        else:
            player = int(line[j])
            castle[player].append((i, j))
            answer[player]+=1

while True:
    isend = True
    for player in range(1, P+1):
        if not castle[player]:
            continue
        queue = castle[player]
        for _ in range(move[player-1]):
            if not queue:
                break
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == ".":
                        board[nr][nc] = str(player)
                        answer[player] += 1
                        queue.append((nr, nc))
                        isend = False
    if isend:
        break

print(*answer[1:])
