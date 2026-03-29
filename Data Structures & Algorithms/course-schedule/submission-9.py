class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjs = [[] for course in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adjs[src].append(dst)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finish = 0
        while q:
            val = q.popleft()
            finish += 1
            for node in adjs[val]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        if finish == numCourses:
            return True
        return False
