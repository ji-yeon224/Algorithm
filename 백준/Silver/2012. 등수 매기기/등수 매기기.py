import sys
input = sys.stdin.readline
N = int(input())
rankList = [int(input()) for _ in range(N)]
rankList.sort()
complain = 0
for index, rank in enumerate(rankList):
    complain += abs(index+1-rank)
print(complain)