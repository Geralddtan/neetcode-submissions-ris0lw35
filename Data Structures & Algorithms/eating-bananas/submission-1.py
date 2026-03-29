class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_possible_speed = max(piles)
        l, r = 1, max_possible_speed
        while l <= r:
            mid = (l+r)//2
            time_taken = self.getTime(piles, mid)
            if time_taken > h:
                l = mid+1
            else:
                r = mid - 1
        
        if self.getTime(piles, mid) > h:
            return mid + 1
        else:
            return mid
    
    def getTime(self, piles, k):
        time = 0
        for pile in piles:
            time += math.ceil(pile/k)
        return time