class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjl = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        for src, dst in prerequisites:
            indegree[dst] += 1
            adjl[src].append(dst)

        q = deque()
        res = []
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            val = q.popleft()
            res.append(val)
            for prereq in adjl[val]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)

        if len(res) != numCourses:
            return []
        return res[::-1]

