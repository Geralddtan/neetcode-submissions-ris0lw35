class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        NUM_FRESH = 0
        q = deque()
        time = 0
        MAX_ROW, MAX_COL = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if grid[row][col] == 1:
                    NUM_FRESH += 1
                if grid[row][col] == 2:
                    q.append([row, col])

        if NUM_FRESH == 0:
            return 0

        while q:
            print(q)
            time += 1
            for i in range(len(q)):
                rotten_x, rotten_y = q.popleft()
                for add_x, add_y in directions:
                    x, y = rotten_x + add_x, rotten_y + add_y
                    if x < MAX_ROW and y < MAX_COL and x >= 0 and y >= 0 and grid[x][y] == 1:
                        NUM_FRESH -= 1
                        grid[x][y] = 2
                        q.append([x,y])
                        if NUM_FRESH == 0:
                            return time
        
        return -1


            

        

        