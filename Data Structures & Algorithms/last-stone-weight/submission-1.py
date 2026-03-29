class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            s1 = -heapq.heappop(maxheap)
            s2 = -heapq.heappop(maxheap)

            remaining = s1-s2
            if remaining >= 1:
                heapq.heappush(maxheap, -remaining)

        if len(maxheap) == 1:
            return -heapq.heappop(maxheap)
        else:
            return 0
