class Solution:
    def solve(self, board: List[List[str]]) -> None:
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        def dfs(i, j):
            if i < 0 or i >= MAX_ROW or j < 0 or j >= MAX_COL or board[i][j] == "X"or board[i][j] == "T":
                return
            
            board[i][j] = "T"
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        for i in range(MAX_ROW):
            dfs(i, 0)
            dfs(i, MAX_COL-1)
        
        for i in range(MAX_COL):
            dfs(0, i)
            dfs(MAX_ROW-1, i)

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"



