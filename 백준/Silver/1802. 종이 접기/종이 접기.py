
import sys
input = sys.stdin.readline

def reverse(arr):
    return [1-i for i in map(int, arr[::-1])]

def divide(arr):
    if len(arr) == 1:
        return True
    length = len(arr)//2
    
    left = arr[:length]
    right = arr[length+1:]
    revRight = reverse(right)
    
    if left != revRight:
        return False
    return divide(left)
    
def solution():
    paper = [i for i in map(int, input().rstrip())]
    if len(paper) < 3:
        print("YES")
    else:
        print("YES") if divide(paper) else print("NO")
    
T = int(input())
for i in range(T):
    solution()
