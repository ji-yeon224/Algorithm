doc = list(input())
word = list(input())
length = len(word)
index = 0
answer = 0
while index < len(doc):
    if doc[index: index+length] == word:
        answer += 1
        index += length
    else:
        index += 1
print(answer)