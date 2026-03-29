class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        q = []
        fresh_fruits = 0
        visited = []

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        if fresh_fruits == 0:
            return 0

        timer = -1
        while q:
            timer += 1
            for index in range(len(q)):
                (i,j) = q.pop(0)
                if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or grid[i][j] == 0 or (i,j) in visited:
                    continue
                
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh_fruits -= 1
                    if fresh_fruits == 0:
                        return timer

                visited.append((i,j))
                
                q.append((i+1,j))
                q.append((i,j+1))
                q.append((i-1,j))
                q.append((i,j-1))
                
        if fresh_fruits == 0:
            return timer
        else:
            return -1
                



