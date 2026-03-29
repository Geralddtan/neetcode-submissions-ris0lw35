class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            if target-value in hash_map:
                return [hash_map[(target-value)], index]
            hash_map[value] = index
        
            