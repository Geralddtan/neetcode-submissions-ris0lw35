class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = 0
        for edge in edges:
            num_nodes = max(num_nodes, edge[0])
            num_nodes = max(num_nodes, edge[1])
        num_nodes += 1
        adjl = [[] for i in range(num_nodes)]
        indegree = [0]*num_nodes

        for src, dst in edges:
            adjl[src].append(dst)
            adjl[dst].append(src)
            indegree[src] += 1
            indegree[dst] += 1

        q = deque()
        for index, degree in enumerate(indegree):
            if degree == 1:
                q.append(index)
        
        while q:
            val = q.popleft()
            for nei in adjl[val]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        cycle = []
        for index, val in enumerate(indegree):
            if val == 2:
                cycle.append(index)

        for edge in edges[::-1]:
            if edge[0] in cycle and edge[1] in cycle:
                return edge


