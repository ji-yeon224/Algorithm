import sys
input = sys.stdin.readline
N, L = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]
pool.sort(key = lambda x: x[0])
boardEnd = pool[0][0]

answer = 0
for start, end in pool:
    if boardEnd > end:
        continue
    elif boardEnd < start:
        boardEnd = start
    
    length = end - boardEnd
    need = length // L
    if length % L > 0:
        need += 1
    boardEnd += need*L
    answer += need
print(answer)