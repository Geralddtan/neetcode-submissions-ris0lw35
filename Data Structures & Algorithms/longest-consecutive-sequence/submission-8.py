class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        
        counter = 0
        for num in nums:
            if num-1 in hashset:
                continue
            
            val = num
            while val in hashset:
                counter += 1
                res = max(res, counter)
                val += 1
            counter = 0
        
        return res

