class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROW = len(heights)
        COL = len(heights[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r, c, visited, prevHeight):
            if (r < 0) or (r >= ROW) or (c < 0) or (c >= COL) or heights[r][c] < prevHeight or (r,c) in visited:
                return

            visited.add((r,c))
            for x,y in directions:
                dfs(r+x, c+y, visited, heights[r][c])

        for row in range(len(heights)):
            dfs(row, 0, pacific, 0)
            dfs(row, COL-1, atlantic, 0)

        for col in range(len(heights[0])):
            dfs(0, col, pacific, 0)
            dfs(ROW-1, col, atlantic, 0)

        print(pacific)
        print(atlantic)
        result = []
        for val in pacific:
            if val in atlantic:
                result.append(list(val))
        
        return result


