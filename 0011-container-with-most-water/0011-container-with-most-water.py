class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        container = 0
        while left < right:
            width = right - left
            minHeight = min(height[left], height[right])
            container = max(container, width*minHeight)
            if height[left] < height[right]:
                left += 1
            else: right -= 1
        return container