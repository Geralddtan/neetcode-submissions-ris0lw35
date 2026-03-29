class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = [[] for i in range(n)]
        visited = set()

        for node1, node2 in edges:
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)

        def dfs(node, prev):            
            if node in visited:
                return False

            visited.add(node)
            for neighbour in adjlist[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False

            return True

        if dfs(0, -1) and len(visited) == n:
            return True
        print(visited)
        return False