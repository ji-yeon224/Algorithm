S = list(input())
T = list(input())
answer = 0

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    if T == S:
        answer = 1
        break
    elif len(T) < len(S):
        break

print(answer)