class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])

        def dfs(row, col, distance):
            if row<0 or row>=MAX_ROW or col<0 or col>=MAX_COL or grid[row][col] == -1:
                return
            
            if grid[row][col] >= distance:
                grid[row][col] = distance
                dfs(row+1, col, distance+1)
                dfs(row, col+1, distance+1)
                dfs(row-1, col, distance+1)
                dfs(row, col-1, distance+1)
                
        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        
                



