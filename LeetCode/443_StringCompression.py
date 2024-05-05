class Solution:
    def compress(self, chars: List[str]) -> int:
        letter = chars[0]
        answerList = []
        answerList.append(letter)
        count = 0
        
        for c in chars:
            if letter == c:
                count += 1
            else:
                if count > 1:
                    answerList += list(map(str, str(count)))
                letter = c
                count = 1
                answerList.append(str(letter))
        if count != 1:
            answerList += list(map(str, str(count)))
        for idx, c in enumerate(chars):
            if idx >= len(answerList):
                del chars[idx:]
                break
            else:
                chars[idx] = answerList[idx]
            

        return len(chars)