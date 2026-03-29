class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_number = 0
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        q = deque()
        visited = set()

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if grid[i][j] == 1:
                    fresh_number += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        if fresh_number == 0:
            return 0

        timer = -1
        while q:
            timer += 1
            for index in range(len(q)):
                i, j = q.popleft()

                if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or (i,j) in visited or grid[i][j] == 0:
                    continue

                if grid[i][j] == 1:
                    grid[i][j] = 2
                    fresh_number -= 1
                    if fresh_number == 0:
                        return timer
                
                visited.add((i,j))

                q.append((i+1, j))
                q.append((i-1, j))
                q.append((i, j+1))
                q.append((i, j-1))
                if fresh_number == 0:
                    return timer

        return timer if fresh_number == 0 else -1
        
