class Solution {
    /** 내 코드 
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        var result: [Bool] = []
        let max = candies.max()!
        
        for i in 0..<candies.count {
            if candies[i] + extraCandies >= max {
                result.append(true)
            } else {
                result.append(false)
            }
        }
        
        return result
    }
    **/

    // 다른 사람 코드..
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        
        let max = (candies.max() ?? 0) - extraCandies
        return candies.map({ $0 >= max })
    }
}