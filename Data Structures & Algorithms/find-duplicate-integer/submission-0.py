class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = nums[0]
        while True:
            if nums[index] == 0:
                return index
            else:
                next_index = nums[index]
                nums[index] = 0
                index = next_index
