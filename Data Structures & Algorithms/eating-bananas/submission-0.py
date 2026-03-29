class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            rate = (r+l)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/rate)
            if total <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res
