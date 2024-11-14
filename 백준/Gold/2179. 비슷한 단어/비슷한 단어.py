import sys
input = sys.stdin.readline

N = int(input())
words = [(input().rstrip(), i) for i in range(N)]

words.sort()

def checkWord(w1, w2):
    minLen = min(len(w1), len(w2))
    for i in range(minLen):
        if w1[i] != w2[i]:
            return i
    return minLen

maxLen = 0
prefixDict = {}
for i in range(N-1):
    if words[i][0] == words[i+1][0]:
        continue
    
    same = checkWord(words[i][0], words[i+1][0])
    
    if maxLen < same:
        
        prefix = words[i][0][:same]
        maxLen = same
        prefixDict.clear()
        prefixDict[prefix] = min(words[i][1], words[i+1][1])
    elif maxLen == same:
        
        prefix = words[i][0][:same]
        if prefix in prefixDict:
            prefixDict[prefix] = min(prefixDict[prefix], words[i+1][1])
        else:
            prefixDict[prefix] = min(words[i][1], words[i+1][1])

minIdx = N
prefix = ''
for p, i in prefixDict.items():
    if minIdx > i:
        prefix = p
        minIdx = i

words.sort(key=lambda x : x[1])
answer = []
for w, i in words:
    if len(w) >= maxLen and w[:maxLen] == prefix:
        answer.append(w)
    if len(answer) == 2:
        break
print(answer[0])
print(answer[1])