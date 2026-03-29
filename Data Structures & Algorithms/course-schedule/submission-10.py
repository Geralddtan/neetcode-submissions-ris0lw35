class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjlist = [[] for i in range(numCourses)]

        for dst, src in prerequisites:
            indegree[dst] += 1
            adjlist[src].append(dst)

        q = []
        for index, val in enumerate(indegree):
            if val == 0:
                q.append(index)

        while q:
            node = q.pop()
            for connection in adjlist[node]:
                indegree[connection] -= 1
            
                if indegree[connection] == 0:
                    q.append(connection)

        for deg in indegree:
            if deg != 0:
                return False
        return True
