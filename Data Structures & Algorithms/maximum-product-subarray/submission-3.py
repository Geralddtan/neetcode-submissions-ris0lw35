class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minCurr, maxCurr = nums[0], nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            newMinCurr = min(nums[i], nums[i]*minCurr, nums[i]*maxCurr)
            newMaxCurr = max(nums[i], nums[i]*minCurr, nums[i]*maxCurr)
            minCurr = newMinCurr
            maxCurr = newMaxCurr
            res = max(res, maxCurr)

        return res