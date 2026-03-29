class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            l, r = index+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r] + nums[index]
                if total == 0:
                    result.append([nums[index], nums[l], nums[r]])
                    l+=1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l+=1
                elif total < 0:
                    l+=1
                else:
                    r -= 1

        return result