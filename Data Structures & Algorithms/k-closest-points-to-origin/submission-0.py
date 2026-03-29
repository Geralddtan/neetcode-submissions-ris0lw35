class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            x,y = point
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        
        res = []
        for i in range(k):
            closest = heapq.heappop(minHeap)
            res.append([closest[1], closest[2]])
        
        return res
