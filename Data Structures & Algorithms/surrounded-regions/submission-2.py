class Solution:
    def solve(self, board: List[List[str]]) -> None:
        MAX_ROW = len(board)
        MAX_COL = len(board[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= MAX_ROW or j >= MAX_COL or board[i][j] == "X" or board[i][j] == "T":
                return

            board[i][j] = "T"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for row in range(MAX_ROW):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][MAX_COL-1] == "O":
                dfs(row, MAX_COL-1)

        for col in range(MAX_COL):
            if board[0][col] == "O":
                dfs(0, col)
            if board[MAX_ROW-1][col] == "O":
                dfs(MAX_ROW-1, col)

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"

            

