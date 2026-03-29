class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        visited = [[False for i in range(MAX_COL)] for j in range(MAX_ROW)]
        q = deque()

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        dist = 0
        while q:
            for index in range(len(q)):
                i, j = q.popleft()
                if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or grid[i][j] == -1 or visited[i][j] == True:
                    continue
                
                visited[i][j] = True
                grid[i][j] = dist
                q.append((i+1,j))
                q.append((i-1,j))
                q.append((i,j+1))
                q.append((i,j-1))
            dist += 1




