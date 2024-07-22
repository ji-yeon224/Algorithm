N, K = map(int, input().split())
nums = list(map(int, input()))
stack = [nums[0]]
for i in range(1, N):
    while stack and stack[-1] < nums[i] and K > 0:
        stack.pop()
        K-=1
    stack.append(nums[i])
print(''.join(map(str, stack[:len(stack)-K])))