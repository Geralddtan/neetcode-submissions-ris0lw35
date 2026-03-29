class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCounter = 0
        for num in nums:
            counter = 0
            val = num
            while val in numSet:
                counter += 1
                val += 1
            maxCounter = max(counter, maxCounter)
        return maxCounter