class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for num in nums:
            if num-1 in hashset:
                continue
            val = num
            count = 0
            while val in hashset:
                count += 1
                res = max(res, count)
                hashset.remove(val)
                val = val+1

        return res