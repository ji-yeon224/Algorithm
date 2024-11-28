def solution(diffs, times, limit):
    answer = 0
    minLevel = 1
    maxLevel = max(diffs)
    while minLevel < maxLevel:
        level = (minLevel + maxLevel)//2
        time = spentTime(level, diffs, times)
        if time > limit:
            minLevel = level + 1
        else:
            maxLevel = level
        
    return maxLevel

def spentTime(level, diffs, times):
    total = times[0]
    for i in range(1, len(diffs)):
        tryCount = diffs[i]-level if diffs[i]-level > 0 else 0
        total += (times[i-1]+times[i])*tryCount + times[i]
    return total
    
        