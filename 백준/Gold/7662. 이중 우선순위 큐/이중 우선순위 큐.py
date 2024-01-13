import heapq
import sys


def solution():
    k = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    numlist = {}
    for _ in range(k):
        input = sys.stdin.readline().split()
        cmd = input[0]
        num = int(input[1])
        if cmd == "I":
            if num in numlist: # 중복
                numlist[num] += 1
            else:
                numlist[num] = 1
                heapq.heappush(minheap, num)
                heapq.heappush(maxheap, -num)
        else:
            if len(numlist) == 0:
                continue
            else:
                if num == -1:
                    while minheap[0] not in numlist:
                        heapq.heappop(minheap)
                    if minheap[0] in numlist:
                        if numlist[minheap[0]] == 1:
                            pop = heapq.heappop(minheap)
                            del(numlist[pop])
                        else:
                            numlist[minheap[0]] -= 1
                    
                else:
                    while -maxheap[0] not in numlist:
                        heapq.heappop(maxheap)
                    if -maxheap[0] in numlist:
                        if numlist[-maxheap[0]] == 1:
                            pop = -heapq.heappop(maxheap)
                            del(numlist[pop])
                        else:
                            numlist[-maxheap[0]] -= 1
                        
    if len(numlist) == 0:
        print("EMPTY")
    else:
        max = -heapq.heappop(maxheap)
        min = heapq.heappop(minheap)
        
        while min not in numlist or numlist[min] == 0:
            min = heapq.heappop(minheap)
        while max not in numlist or numlist[max] == 0:
            max = -heapq.heappop(maxheap)
        print(max, min)


t = int(sys.stdin.readline())
for _ in range(t):
    solution()