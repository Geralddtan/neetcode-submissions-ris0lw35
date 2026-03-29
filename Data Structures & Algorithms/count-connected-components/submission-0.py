class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjl = [[] for i in range(n)]
        for edge in edges:
            adjl[edge[0]].append(edge[1])
            adjl[edge[1]].append(edge[0])
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjl[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i,-1)
        
        return res
