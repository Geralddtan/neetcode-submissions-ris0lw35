class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, total, i):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(subset)
                return
            
            backtrack(subset.copy(), total, i+1)
            subset.append(nums[i])
            backtrack(subset.copy(), total+nums[i], i)

        backtrack([], 0, 0)
        return res