class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, pointer):
            if pointer == len(nums):
                res.append(subset.copy())
                return

            backtrack(subset.copy(), pointer+1)
            subset.append(nums[pointer])
            backtrack(subset.copy(), pointer+1)

        backtrack([], 0)
        return res