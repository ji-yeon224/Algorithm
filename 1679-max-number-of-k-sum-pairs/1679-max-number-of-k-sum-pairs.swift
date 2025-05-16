class Solution {
    func maxOperations(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.filter { $0 < k }
        var (left, right) = (0, nums.count-1)
        var answer = 0
        for i in 0..<nums.count {
            while left < right {
                let (leftNum, rightNum) = (nums[left], nums[right])
                if leftNum != -1, leftNum+rightNum == k {
                    answer += 1
                    nums[left] = -1
                    nums[right] = -1
                    break
                }
                left += 1
            }
            right -= 1
            left = 0
        }
        return answer
    }
}