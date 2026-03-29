class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x,y in points:
            distance = x**2 + y**2
            minheap.append([distance, x, y])

        heapq.heapify(minheap)

        for i in range(k):
            point = heapq.heappop(minheap)
            res.append([point[1], point[2]])

        return res

