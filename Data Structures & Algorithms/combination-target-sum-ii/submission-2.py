class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, total, i):
            if total == target:
                res.append(subset)
                return
            elif total > target or i >= len(candidates):
                return 

            subset.append(candidates[i])
            backtrack(subset.copy(), total + candidates[i], i+1)
            subset.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1

            backtrack(subset.copy(), total, i+1)
                
        backtrack([], 0, 0)
        return res

