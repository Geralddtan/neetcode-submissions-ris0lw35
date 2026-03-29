class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adjlist= [[] for i in range(numCourses)]
        q = deque()
        res = []

        for dest, src in prerequisites:
            adjlist[src].append(dest)
            indegree[dest] += 1

        for index, deg in enumerate(indegree):
            if deg == 0:
                q.append(index)

        while q:
            node = q.popleft()
            res.append(node)
            for neighbour in adjlist[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if len(res) != numCourses:
            return []
        return res

        

