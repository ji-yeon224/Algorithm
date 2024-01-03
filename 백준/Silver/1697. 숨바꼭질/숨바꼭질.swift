
import Foundation

func solution() -> Int {
    
    let input = readLine()!.components(separatedBy: " ").map { Int("\($0)")!}
    var start = input[0]
    var dest = input[1]
    
    if start >= dest {
        return input[0]-input[1]
    }
    
    if start*2 == dest {
        return 1
    }
    
    var dp = Array.init(repeating: 100001, count: dest+1)
    
    for i in 0..<start {
        dp[i] = start - i
    }
    
    dp[start] = 0
    
    for i in start+1...dest {
        if i % 2 == 0 {
            dp[i] = min(dp[i/2] + 1, dp[i-1]+1)
        } else {
            dp[i] = min(dp[i-1] + 1, dp[(i+1)/2] + 2)
            
        }
        
    }
    return dp[dest]
    
}

print(solution())
