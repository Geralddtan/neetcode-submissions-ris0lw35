class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for key, value in enumerate(nums):
            l, r = key + 1, len(nums)-1
            if key > 0 and value == nums[key-1]:
                continue
            while l < r:
                current_val = value + nums[l] + nums[r]
                if current_val > 0:
                    r -= 1
                    continue
                elif current_val < 0:
                    l += 1
                else:
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return result

