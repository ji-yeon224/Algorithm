from functools import reduce
num = int(input())
line = list(map(int, input().split()))
line.sort()

for i in range(1, num):
    line[i] += line[i-1]

result = reduce(lambda x, y: x + y, line)
print(result)