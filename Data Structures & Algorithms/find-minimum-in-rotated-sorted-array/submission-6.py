class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l < r:
            mid = (l+r)//2
            print(l,r,nums[mid])
            if nums[r] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid + 1
        return nums[l]


# 1,2,3,4,5,6
# 6,1,2,3,4,5
# 5,6,1,2,3,4
# 4,5,6,1,2,3
# 3,4,5,6,1,2
# 2,3,4,5,6,1

# if your right is smaller than you, your right is the answer
# if your right is larger than you, 