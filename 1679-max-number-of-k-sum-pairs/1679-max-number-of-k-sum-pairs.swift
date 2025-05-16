class Solution {
    func maxOperations(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.filter { $0 < k }
        nums = nums.sorted()
        var (left, right) = (0, nums.count-1)
        var answer = 0
        while left < right {
            let sum = nums[left] + nums[right]
            if sum == k {
                answer += 1
                left += 1
                right -= 1
            } else if sum < k {
                left += 1
            } else {
                right -= 1
            }
        }
        return answer
    }
}