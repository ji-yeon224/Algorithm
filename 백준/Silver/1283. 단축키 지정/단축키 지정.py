import sys
input = sys.stdin.readline

N = int(input())
shorts = []

def makeShortsOption(word, index):
    word.insert(index, "[")
    word.insert(index+2, "]")
    return "".join(word)
    
def findShorts(word):
    wordList = [w for w in map(str, word.split(" "))]
    
    for i in range(len(wordList)):
        firstChar = wordList[i][0].upper()
        if firstChar not in shorts:
            wordList[i] = makeShortsOption(list(wordList[i]), 0)
            shorts.append(firstChar)
            return " ".join(wordList)
            
    for i in range(len(wordList)):
        charList = list(wordList[i])
        for j in range(len(charList)):
            checkChar = charList[j].upper()
            if checkChar not in shorts:
                wordList[i] = makeShortsOption(charList, j)
                shorts.append(checkChar)
                return " ".join(wordList)
    
    return " ".join(wordList)

for _ in range(N):
    word = input().rstrip()
    result = findShorts(word)
    print(result)