class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index in range(len(nums)):
            if (nums[index]) in dic:
                return sorted([index, dic[nums[index]]])
            else:
                dic[target - nums[index]] = index
    