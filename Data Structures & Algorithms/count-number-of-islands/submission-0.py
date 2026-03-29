class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        number_islands = 0

        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for x, y in directions:
                dfs(r+x, c+y)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    number_islands += 1
                    dfs(row, col)

        return number_islands
