class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, i, total):
            nonlocal res
            if total == target:
                res.append(subset)
                return
            if total > target:
                return
            if i >= len(nums):
                return

            backtrack(subset.copy(), i+1, total)
            subset.append(nums[i])
            backtrack(subset.copy(), i, total + nums[i])

            
        backtrack([], 0, 0)
        return res
