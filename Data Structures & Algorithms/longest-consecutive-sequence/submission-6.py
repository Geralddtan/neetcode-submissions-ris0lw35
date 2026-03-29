class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
        longest = 1
        for num in nums:
            i = 1
            while num+i in hashset:
                longest = max(longest, i+1)
                i += 1

        return longest