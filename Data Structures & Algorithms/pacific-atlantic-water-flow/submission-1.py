class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        MAX_ROW = len(heights)
        MAX_COL = len(heights[0])

        def dfs(i, j, visit, prevHeight):
            if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or heights[i][j] < prevHeight or (i,j) in visit:
                return

            visit.add((i,j))
            height = heights[i][j]
            dfs(i+1, j, visit, height)
            dfs(i-1, j, visit, height)
            dfs(i, j+1, visit, height)
            dfs(i, j-1, visit, height)
            
        for col in range(MAX_COL):
            dfs(0, col, pac, 0)
            dfs(MAX_ROW-1, col, atl, 0)

        for row in range(MAX_ROW):
            dfs(row, 0, pac, 0)
            dfs(row, MAX_COL-1, atl, 0)

        res = []
        print(pac, atl)
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i,j])
        
        return res
