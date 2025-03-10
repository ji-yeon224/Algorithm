class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Len = len(word1)
        word2Len = len(word2)
        maxLen = max(word1Len, word2Len)
        newStr = ""
        for i in range(maxLen):
            if i < word1Len:
                newStr += word1[i]
            if i < word2Len:
                newStr += word2[i]
        return newStr
        