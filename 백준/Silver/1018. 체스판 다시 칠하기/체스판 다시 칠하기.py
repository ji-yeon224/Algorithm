N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
result = []
for i in range(N-7):
    for j in range(M-7):
        startW = 0
        startB = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] == 'W':
                        startB += 1
                    if board[k][l] == 'B':
                        startW += 1
                else:
                    if board[k][l] == 'B':
                        startB += 1
                    if board[k][l] == 'W':
                        startW += 1
        result.append(startW)
        result.append(startB)
print(min(result))
