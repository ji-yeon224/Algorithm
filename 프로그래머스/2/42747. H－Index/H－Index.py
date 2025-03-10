def solution(citations):
    count = len(citations)
    citations.sort()
    for i in range(count):
        if citations[i] >= count - i:
            return count - i
    return 0