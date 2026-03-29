class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_ls = []
        for k in range(len(nums)):
            left, right = k + 1, len(nums)-1
            if k > 0 and nums[k] == nums[k-1] :
                continue
            while left < right:
                total = nums[left] + nums[right] + nums[k]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    final_ls.append([nums[left], nums[right], nums[k]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
        return final_ls


        