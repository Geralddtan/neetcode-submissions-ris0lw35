class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        volume = 0
        while left < right:
            volume = max(volume, min(heights[left], heights[right]) * (right - left))
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        return volume