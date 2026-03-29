class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        tracked = set()
        prereqs = defaultdict(list)
        for req in prerequisites:
            prereqs[req[0]].append(req[1])
        res = []

        def dfs(course):
            nonlocal res
            reqs = prereqs[course]
            visited.add(course)
            tracked.add(course)
            for req in reqs:
                if req in visited:
                    return
                if req not in tracked:
                    dfs(req)
            visited.remove(course)
            res.append(course)
        
        for course in range(numCourses):
            if course not in tracked:
                dfs(course)

        if len(res) != numCourses:
            return []

        return res
