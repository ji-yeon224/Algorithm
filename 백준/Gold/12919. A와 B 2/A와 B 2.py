S = input()
T = input()
length = len(S)
isChange = 0

def makeWord(cur):
    global S, isChange
     
    if isChange == 1:
        return
    
    if len(cur) == length:
        if cur == S:
            isChange = 1
        return
    if cur[-1] == 'A':
        w = cur[:len(cur)-1]
        makeWord(w)
    if cur[0] == 'B':
        w = cur[1:]
        makeWord(w[::-1])
    
makeWord(T)
print(isChange)