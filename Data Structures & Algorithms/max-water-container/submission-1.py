class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = min(heights[l], heights[r]) * (r-l)

        while l < r-1:
            if heights[l] < heights[r]:
                l += 1
                while heights[l] < heights[l-1]:
                    l += 1
                new_area = min(heights[l], heights[r]) * (r-l)
                max_area = max(max_area, new_area)
            else:
                r -= 1
                while heights[r] < heights[r+1]:
                    r -= 1
                new_area = min(heights[l], heights[r]) * (r-l)
                max_area = max(max_area, new_area)
            
        max_area = max(max_area, min(heights[l], heights[r]) * (r-l))

        return max_area
