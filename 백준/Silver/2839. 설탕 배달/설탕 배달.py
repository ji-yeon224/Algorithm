import sys
N = int(sys.stdin.readline())

result = 0

while N >= 0:
    if N % 5 == 0:
        result += int(N//5)
        print(result)
        break
    N -= 3
    result += 1  
    
else:
    print(-1)