class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        [-4,-1,-1,0,1,2]
        [0,0,0,0]
        result = []
        for index, value in enumerate(nums):
            if value > 0:
                break

            if index > 0 and value == nums[index-1]:
                continue

            l, r = index+1, len(nums)-1
            while l < r:
                sum_total = nums[l] + nums[r] + value
                if sum_total < 0:
                    l += 1
                elif sum_total > 0:
                    r -= 1
                else:
                    result.append([value, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
            
        return result
