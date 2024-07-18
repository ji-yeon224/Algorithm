from collections import defaultdict 
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input()
    K = int(input())
    
    minLen = len(string)+1
    maxLen = 0
    dict = defaultdict(list)
    for i in range(len(string)):
        if string.count(string[i]) >= K:
            dict[string[i]].append(i)
    
    if not dict:
        print(-1)
        continue
    
    for char in dict:
        indexList = dict[char]
        for i in range(len(indexList) - K + 1):
            length = indexList[i+K-1] - indexList[i] + 1
            minLen = min(minLen, length)
            maxLen = max(maxLen, length)
    print(minLen, maxLen)