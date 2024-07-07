word = input().upper()
wordList = set(word)
countList = [[word.count(w), w] for w in wordList]
countList.sort(reverse = True)
if len(countList) <= 1:
    print(countList[0][1])
else:
    if countList[0][0] == countList[1][0]:
        print("?")
    else:
        print(countList[0][1])