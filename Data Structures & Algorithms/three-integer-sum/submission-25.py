class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        [-4,-1,-1,0,1,2]
        index = 0
        while index < len(nums):
            target = 0 - nums[index]
            l, r = index+1, len(nums)-1
            while l < r:
                total_sum = nums[l] + nums[r]
                if total_sum == target:
                    res.append([nums[index],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif total_sum < target:
                    l += 1
                else:
                    r -= 1

            index += 1
            while index < len(nums) and nums[index] == nums[index-1]:
                index += 1
        return res


