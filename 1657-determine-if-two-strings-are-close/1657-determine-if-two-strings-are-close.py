class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Arr = list(word1)
        word2Arr = list(word2)
        word1Arr.sort()
        word2Arr.sort()
        
        word1Set = set(word1Arr)
        word2Set = set(word2Arr)
        if word1Set != word2Set:
            return False
        word1Dict = {c: 0 for c in word1Set}
        word2Dict = {c: 0 for c in word2Set}

        for i in range(len(word1Arr)):
            word1Dict[word1Arr[i]] += 1
            word2Dict[word2Arr[i]] += 1
        word1Counts = word1Dict.values()
        word2Counts = word2Dict.values()
        if sorted(word1Counts) == sorted(word2Counts):
            return True
        else: return False
