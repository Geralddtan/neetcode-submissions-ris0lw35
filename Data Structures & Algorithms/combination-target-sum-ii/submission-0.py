class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, subset, total):
            nonlocal res
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            
            subset.append(candidates[i])
            backtrack(i+1, subset.copy(), total + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, subset.copy(), total)

        backtrack(0, [], 0)
        return res

        [1,2,2,4,5,6,9]
