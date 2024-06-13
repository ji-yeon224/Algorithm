N = int(input())
score = [int(input()) for _ in range(N)]
answer = 0
if N == 1:
    print(answer)
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        while score[i] >= score[i+1]:
            score[i] -= 1
            answer += 1
print(answer)