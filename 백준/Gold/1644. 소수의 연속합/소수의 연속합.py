import math

N = int(input())

if N == 1:
    print(0)
    exit(0)

isPrime = [True]*(N+1)
isPrime[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if isPrime[i]:
        for j in range(2*i, N+1, i):
            isPrime[j] = False
primeNums = [i for i in range(2, N+1) if isPrime[i]]

left = 0
right = 0
answer = 0
totalSum = primeNums[0]

while left <= right:
    
    if totalSum <= N:
        if totalSum == N:
            answer += 1
        right += 1
        if right == len(primeNums):
            break
        totalSum += primeNums[right]
    elif totalSum > N:
        totalSum -= primeNums[left]
        left += 1
    
print(answer)  
