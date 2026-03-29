class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROW = len(grid)
        COL = len(grid[0])
        FRESH_FRUITS = 0
        TIME = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    FRESH_FRUITS += 1

        if FRESH_FRUITS == 0:
            return 0

        while q:
            num_rotten = len(q)
            print(q)
            for i in range(num_rotten):
                row, col = q.popleft()

                for x,y in directions:
                    new_x, new_y = row+x, col+y
                    if new_x >= 0 and new_x < ROW and new_y >= 0 and new_y < COL and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                
                if grid[row][col] == 1:
                    print(row,col)
                    grid[row][col] = 2
                    FRESH_FRUITS -= 1
                    if FRESH_FRUITS == 0:
                        return TIME
            TIME += 1

        return -1
