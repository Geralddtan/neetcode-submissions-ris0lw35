class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap =[-stone for stone in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            s1 = -heapq.heappop(minHeap)
            s2 = -heapq.heappop(minHeap)
            
            if s1 < s2:
                heapq.heappush(minHeap, s1-s2)
            if s2 < s1:
                heapq.heappush(minHeap, s2-s1)
            
        if minHeap:
            last_stone = heapq.heappop(minHeap)
            return -last_stone
        else:
            return 0

            
            
