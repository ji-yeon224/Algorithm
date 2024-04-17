import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [n for n in map(int, input().split())]

tab = []
answer = 0

for i, item in enumerate(items):
    if item in tab:
        continue
    if len(tab) < N:
        tab.append(item)
    else:
        
        answer += 1
        remove = -1
        nxtItems = items[i+1:]
        target = 0
        
        for t in tab:
            if t in nxtItems:
                if remove < nxtItems.index(t):
                    remove = nxtItems.index(t)
                    target = t
            else:
                target = t
                break
        tab[tab.index(target)] = item   

print(answer)