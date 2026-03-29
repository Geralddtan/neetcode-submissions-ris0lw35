class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        visited = [[False for i in range(MAX_COL)] for j in range(MAX_ROW)]
        q = deque()

        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if grid[row][col] == 0:
                    q.append((row, col))

        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row < 0 or col < 0 or row >= MAX_ROW or col >= MAX_COL or visited[row][col] == True or grid[row][col] == -1:
                    continue
                
                visited[row][col] = True
                grid[row][col] = distance
                q.append((row+1, col))
                q.append((row, col+1))
                q.append((row-1, col))
                q.append((row, col-1))
                
            distance += 1

        
                    

