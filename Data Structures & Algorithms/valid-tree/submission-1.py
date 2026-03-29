class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjl = [[] for i in range(n)]
        for edge in edges:
            adjl[edge[0]].append(edge[1])
            adjl[edge[1]].append(edge[0])
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)    
            neighbors = adjl[node]
            for neighbor in neighbors:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        if dfs(0,-1) and len(visited) == n:
            return True
        return False
        
