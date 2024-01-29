import sys

T = int(sys.stdin.readline())

def maxSticker():
    n = int(sys.stdin.readline())
    sticker = [[int(num) for num in sys.stdin.readline().split()] for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    
    
    
    if n == 1:
        return max(sticker[0][0], sticker[1][0])
    
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + dp[1][0]
    dp[1][1] = sticker[1][1] + dp[0][0]
    
    if n == 2:
        return max(dp[0][1], dp[1][1])

    for i in range(2, n):
        preMax = max(dp[0][i-2], dp[1][i-2])
        dp[0][i] = max(preMax, dp[1][i-1]) + sticker[0][i]
        dp[1][i] = max(preMax, dp[0][i-1]) + sticker[1][i]
    
    return max(dp[0][-1], dp[1][-1])
    
  
  
for _ in range(T):
    print(maxSticker())