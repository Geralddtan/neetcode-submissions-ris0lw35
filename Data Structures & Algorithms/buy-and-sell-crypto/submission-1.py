class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0

        l, r = 0, 1
        while r < len(prices)-1 and prices[r] < prices[l]:
            l += 1
            r += 1

        max_profit = prices[r] - prices[l]
        while r < len(prices):
            while r < len(prices)-1 and prices[r+1] > prices[r]:
                r += 1

            max_profit = max(max_profit, prices[r] - prices[l])
            if r < len(prices)-1 and prices[r+1] < prices[l]:
                l = r+1
                r = l+1
            else:
                r += 1
            
        return max(0, max_profit)

            

