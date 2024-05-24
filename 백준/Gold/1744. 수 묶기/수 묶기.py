N = int(input())

plus = []
minus = []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort(reverse = True)
minus.sort()
plusLen = len(plus)
minusLen = len(minus)

index = 0
total = 0
while index < plusLen:
    if index + 1 < plusLen:
        num = plus[index] * plus[index+1]
        if num > plus[index]:
            total += num
            index += 2
        else:
            total += plus[index]
            index += 1
    else:
        total += plus[index]
        index += 1

index = 0
while index < minusLen:
    if index + 1 < minusLen:
        num = minus[index] * minus[index+1]
        total += num
        index += 2
    else:
        total += minus[index]
        index += 1
print(total)
