import sys
input = sys.stdin.readline
L, C = map(int, input().split())
charList = [c for c in input().split()]
charList.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

def password(idx, pw, v):
    global L, C
    if len(pw) == L:
        if v > 0 and len(pw)-v >= 2:
            print(pw)
        return
    for i in range(idx+1, C):
        password(i, pw+charList[i], v+1 if charList[i] in vowels else v)

for i in range(0, C-L+1):
    password(i, charList[i], 1 if charList[i] in vowels else 0)