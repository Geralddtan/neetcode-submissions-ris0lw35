class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        path = []

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if min(r,c) < 0 or r >= MAX_ROW or c >= MAX_COL or board[r][c]!=word[i] or (r,c) in path:
                return False

            path.append((r,c))
            res = dfs(r,c+1,i+1) or dfs(r,c-1,i+1) or dfs(r+1, c,i+1) or dfs(r-1, c, i+1)
            path.remove((r,c))
            return res

        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False

