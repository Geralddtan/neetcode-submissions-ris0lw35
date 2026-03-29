class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minCurr, maxCurr = 1,1

        for n in nums:
            tmp = maxCurr
            maxCurr = max(n*tmp, n*minCurr, n)
            minCurr = min(n*tmp, n*minCurr, n)
            res = max(res, maxCurr)
        
        return res

