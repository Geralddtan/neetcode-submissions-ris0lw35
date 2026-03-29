class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_value = max(max_value, cur_sum)
        
        return max_value