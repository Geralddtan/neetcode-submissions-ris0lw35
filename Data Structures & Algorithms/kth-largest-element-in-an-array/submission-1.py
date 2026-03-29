class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        minheap = heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        res = heapq.heappop(nums)
        return -res