code = [0]+list(map(int, list(input())))
length = len(code)

if code[1] == 0:
    print(0)
else:
    dp = [0]*length
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, length):
        if code[i] > 0:
            dp[i] = dp[i-1]
        num = code[i-1]*10 + code[i]
        if num >= 10 and num <= 26:
            dp[i] += dp[i-2]
    print(dp[-1]%1000000)