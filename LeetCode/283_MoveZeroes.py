class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        front = 0
        rear = len(nums)
        while front < rear:
            if nums[front] == 0:
                del nums[front]
                nums.append(0)
                rear -= 1
            else:
                front += 1