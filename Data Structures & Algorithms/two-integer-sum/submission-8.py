class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {num:index for index,num in enumerate(nums)}
        for index, num in enumerate(nums):
            if (target-num) in hashset and index != hashset[target-num]:
                return [index, hashset[target-num]]
            
