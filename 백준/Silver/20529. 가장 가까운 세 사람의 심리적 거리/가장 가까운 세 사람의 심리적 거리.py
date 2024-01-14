import sys
from itertools import combinations, permutations

def score(m1, m2):
    score = 4
    for i in range(4):
        if m1[i] == m2[i]:
            score -= 1
    return score

def solution():
    n = int(sys.stdin.readline())
    minScore = 12
    mbti = sys.stdin.readline().strip().split()
    
    if n > 32:
        return 0
    
    for com in list(combinations(mbti, 3)):
        total = 0
        total += score(com[0], com[1])
        total += score(com[0], com[2])
        total += score(com[1], com[2])
        minScore = min(minScore, total)
    return minScore
    

t = int(sys.stdin.readline())

for _ in range(t):
    print(solution())