class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        def dfs(course):
            print(course, visited)
            if course in visited:
                return False

            visited.add(course)
            prereq = [req for req in prerequisites if req[0] == course]
            for req in prereq:
                if not dfs(req[1]):
                    return False
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True
