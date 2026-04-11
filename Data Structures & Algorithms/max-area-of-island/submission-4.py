class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAX_ROW, MAX_COL = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i, j-1)

        res = 0
        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        
        return res
