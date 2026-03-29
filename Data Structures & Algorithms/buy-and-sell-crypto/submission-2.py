class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while l < len(prices):
            if r < len(prices) and prices[r] >= prices[l]:
                res = max(res, prices[r]-prices[l])
                r += 1
            else:
                l = r
        
        return res
            