class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, i):
            nonlocal res
            if sum(subset) == target:
                res.append(subset)
                return
            elif sum(subset) > target or i >= len(candidates):
                return


            subset.append(candidates[i])            
            backtrack(subset.copy(), i+1)
            subset.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(subset.copy(), i+1)

        backtrack([],0)
        return res
