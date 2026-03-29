class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, subset, total):
            if i>=len(nums) or total > target:
                return
            if total == target:
                res.append(subset.copy())
                return
            
            backtrack(i+1, subset.copy(), total)
            subset.append(nums[i])
            backtrack(i, subset.copy(), total + nums[i])
        
        backtrack(0, [], 0)
        return res
