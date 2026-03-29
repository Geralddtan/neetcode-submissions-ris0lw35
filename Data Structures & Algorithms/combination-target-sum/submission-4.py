class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, i):
            nonlocal res
            if sum(subset) > target or i >= len(nums):
                return
            elif sum(subset) == target:
                res.append(subset)
                return

            backtrack(subset.copy(), i+1)
            subset.append(nums[i])
            backtrack(subset.copy(), i)

        backtrack([], 0)
        return res