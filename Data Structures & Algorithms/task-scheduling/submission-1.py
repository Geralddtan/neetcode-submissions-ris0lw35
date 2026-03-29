class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []
        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        
        for key, value in dic.items():
            maxheap.append([value, key])

        heapq.heapify_max(maxheap)
        q = deque()

        time = 0
        while maxheap or q:
            time += 1
        
            if q and q[0][0] == time:
                node = q.popleft()
                heapq.heappush_max(maxheap, [node[1], node[2]])

            if maxheap:
                task = heapq.heappop_max(maxheap)
                if task[0] > 1:
                    q.append([time + n + 1, task[0]-1, task[1]])

        return time
             

             
