import Foundation
var result = 0
func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    var sum = 0
    var idx = 0
    dfs(sum, numbers, idx, numbers.count, target)
    return result
}

func dfs(_ sum: Int,_ numbers: [Int], _ idx: Int, _ length: Int, _ target: Int) {
    if idx == length {
        if sum == target {
            result += 1
        }
        return
    }
    
    dfs(sum+numbers[idx], numbers, idx+1, length, target)
    dfs(sum-numbers[idx], numbers, idx+1, length, target)
    
    
}