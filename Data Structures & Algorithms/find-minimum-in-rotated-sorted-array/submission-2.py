class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (r+l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] <= nums[r]:
                r = mid
            
        mid = (r+l)//2
        return nums[mid]

# 1,2,3,4,5,6
# 2,3,4,5,6,1
# 3,4,5,6,1,2
# 4,5,6,1,2,3
# 5,6,1,2,3,4
# 6,1,2,3,4,5