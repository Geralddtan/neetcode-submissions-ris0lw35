class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = defaultdict(list)
        for after, before in prerequisites:
            pre_reqs[after].append(before)
        
        def dfs(to_visit, visited):
            if to_visit not in pre_reqs:
                return True
            if to_visit in visited:
                return False

            need_to_finish_first = pre_reqs[to_visit]
            visited.append(to_visit)
            for course in need_to_finish_first:
                if not dfs(course, visited):
                    return False
            
            return True
                
                        
        for course in range(numCourses):
            print("start with course: " + str(course))
            if not dfs(course, []):
                return False

        return True


