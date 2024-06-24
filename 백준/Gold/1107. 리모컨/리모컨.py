N = int(input())
M = int(input())
breakNum = []
if M > 0:
    breakNum = list(map(int, input().split()))
 
if N == 100:
    print(0)
else:
    answer = abs(100-N)
    for i in range(1000000):
        for j in str(i):
            if int(j) in breakNum:
                break
        else:
            answer = min(answer, abs(i-N)+len(str(i)))
    print(answer)