class Solution:

    def __init__(self, w: List[int]):
        self.weight = [0]
        for i in w:
            self.weight.append(self.weight[-1] + i)

    def pickIndex(self) -> int:
        val = random.randint(1, self.weight[-1])

        l, r = 0, len(self.weight)-1
        while l <= r:
            mid = (l+r)//2
            if val <= self.weight[mid] and val > self.weight[mid-1]:
                return mid-1
            elif val > self.weight[mid]:
                l = mid + 1
            else:
                r = mid - 1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()