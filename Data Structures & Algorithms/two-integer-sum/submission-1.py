class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            if (target-value) in dic:
                return [dic[target-value], index]
            dic[value] = index