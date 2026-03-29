class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            l, r = index+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r] + nums[index]
                if total == 0:
                    res.append([nums[l], nums[r], nums[index]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
    
        return res

        [-4,-1,-1,0,1,2]
            
        
