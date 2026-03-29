class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        MAX_AREA = 0

        def dfs(row, col):
            if row >= 0 and row < MAX_ROW and col >= 0 and col < MAX_COL and grid[row][col] == 1:
                grid[row][col] = 0
                return 1 + dfs(row+1, col) + dfs(row, col+1) + dfs(row-1, col) + dfs(row, col-1)
            return 0

        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if grid[row][col] == 1:
                    MAX_AREA = max(MAX_AREA, dfs(row, col))
        
        return MAX_AREA

