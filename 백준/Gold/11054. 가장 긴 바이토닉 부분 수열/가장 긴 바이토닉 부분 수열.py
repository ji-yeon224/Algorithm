import sys

N = int(sys.stdin.readline())
list = [int(n) for n in sys.stdin.readline().split()]
reverse = list[::-1]

increase = [1] * N
decrease = [1] * N

for i in range(1, N):
    for j in range(i):
        if list[i] > list[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse[i] > reverse[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)
decrease.reverse()
maxSum = 0
for i in range(N):
    maxSum = max(maxSum, increase[i]+decrease[i])
print(maxSum-1)