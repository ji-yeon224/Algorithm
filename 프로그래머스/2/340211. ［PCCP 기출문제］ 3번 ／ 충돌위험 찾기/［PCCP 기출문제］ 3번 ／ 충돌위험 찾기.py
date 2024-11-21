from collections import defaultdict


def solution(points, routes):
    secondsDict = defaultdict(set)
    conflictDict = defaultdict(set)
    robotCnt = len(routes)
    conflict = 0
    
    for i in range(robotCnt):
        second = 0
        for j in range(len(routes[i])-1):
            startR, startC = points[routes[i][j]-1]
            destR, destC = points[routes[i][j+1]-1]
            
            curR = startR
            curC = startC
            rMoveCnt = abs(destR - startR)
            cMoveCnt = abs(destC - startC)
            if j == 0:
                if (startR, startC) in secondsDict[second]:
                    conflictDict[second].add((startR, startC))
                secondsDict[second].add((startR, startC))
                second += 1
            
            for _ in range(rMoveCnt+cMoveCnt):
                if curR != destR:
                    if curR < destR: curR += 1
                    else: curR -= 1
                else:
                    if curC < destC: curC += 1
                    else: curC -= 1
                if (curR, curC) in secondsDict[second]:
                    conflictDict[second].add((curR, curC))
                secondsDict[second].add((curR, curC))
                second += 1

    for item in conflictDict.values():
        conflict += len(item)
        
    return conflict
    