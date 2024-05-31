def checkPalindrome(word):
    answer = 0
    left = 0
    right = len(word)-1
    while left < right:
        if word[right] == word[left]:
            right -= 1
            left += 1
        else:
            if word[right-1] == word[left]:
                temp = word[left:right]
                if temp == temp[::-1]:
                    answer = 1
                    break
            if word[left+1] == word[right]:
                temp = word[left+1:right+1]
                if temp == temp[::-1]:
                    answer = 1
                    break
            answer = 2
            break     
    return answer

T = int(input())
for _ in range(T):
    word = list(input())
    print(checkPalindrome(word))