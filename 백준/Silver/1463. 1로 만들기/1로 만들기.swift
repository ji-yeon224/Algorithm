import Foundation
func solution(_ num: Int) -> Int {
    
    if num == 1 { return 0 } 
    else if num == 2 { return 1 }
    else if num == 3 { return 1 }
    
    var dp = Array(repeating: 0, count: num+1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    
    for i in 4...num {
        dp[i] = dp[i-1] + 1
        if i % 3 == 0 {
            dp[i] = min(dp[i], dp[i/3] + 1)
        }
        if i % 2 == 0 {
            dp[i] = min(dp[i], dp[i/2]+1)
        }
    }
    return dp[num]
}

let num = Int(readLine()!)!
print(solution(num))