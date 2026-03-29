class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        # Find pivot
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l
        res = self.binary_search(nums[l:], target)
        if res != -1:
            return res+l
        else:
            return self.binary_search(nums[:l], target)

    
    def binary_search(self, nums, target):
        l,r=0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            print(l,r,nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


# 1,2,3,4,5,6
# 6,1,2,3,4,5
# 5,6,1,2,3,4
# 4,5,6,1,2,3
# 3,4,5,6,1,2
# 2,3,4,5,6,1