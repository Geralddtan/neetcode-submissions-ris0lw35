class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        hashset = set(nums)
        for num in nums:
            if num-1 in hashset:
                continue
            counter = 1
            val = num
            while val+1 in hashset:
                counter += 1
                val+=1
                res = max(res, counter)
        
        return res
