class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = []

        for num in numSet:
            count = 1
            val = num
            while val + count in numSet:
                count += 1
            longest.append(count)
        
        if len(longest) > 0:
            return max(longest)
        else:
            return 0

