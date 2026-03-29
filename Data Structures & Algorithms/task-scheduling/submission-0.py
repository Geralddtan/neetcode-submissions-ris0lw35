class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                val = heapq.heappop(maxHeap)
                if val+1<0:
                    q.append([val+1, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, (q.popleft()[0]))
            
        return time

        