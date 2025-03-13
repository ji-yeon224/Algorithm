import Foundation

func dfs(sum: Int, index: Int, numbers: [Int], target: Int) -> Int {
    if index == numbers.count {
        if sum == target {
            return 1
        }
        return 0
    } 
    
    let plus = dfs(sum: sum+numbers[index], index: index+1, numbers: numbers, target: target)
    let minus = dfs(sum: sum-numbers[index], index: index+1, numbers: numbers, target: target)
    return plus + minus
}

func solution(_ numbers:[Int], _ target:Int) -> Int {
    return dfs(sum: 0, index: 0, numbers: numbers, target: target)
}