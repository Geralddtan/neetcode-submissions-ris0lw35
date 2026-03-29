class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = []
        adjlist = [[] for i in range(n)]
        result = 0

        for src, dest in edges:
            adjlist[src].append(dest)
            adjlist[dest].append(src)

        def dfs(node):
            if node in visited:
                return
            visited.append(node)
            for neighbour in adjlist[node]:
                dfs(neighbour)

        for i in range(n):
            if i not in visited:
                result += 1
                dfs(i)

        return result

