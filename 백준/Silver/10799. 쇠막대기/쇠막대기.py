
bar = list(input())
stack = []
count = 0

for i in range(len(bar)):
    b = bar[i]
    if b == '(':
        stack.append(b)
    elif b == ')':
        stack.pop()
        if bar[i-1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)