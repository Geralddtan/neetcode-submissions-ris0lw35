class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = [[] for i in range(numCourses)]
        q = deque()

        for target, source in prerequisites:
            indegree[target] += 1
            adjList[source].append(target)

        for index, val in enumerate(indegree):
            if val == 0:
                q.append(index)

        while q:
            node = q.popleft()
            neighbours = adjList[node]
            for neighbour in neighbours:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        for val in indegree:
            if val != 0:
                return False
        return True

