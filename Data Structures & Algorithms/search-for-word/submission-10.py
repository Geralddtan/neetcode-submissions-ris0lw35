class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW = len(board)
        MAX_COL = len(board[0])
        visited = set()

        def backtrack(i, j, index):
            if i >= MAX_ROW or i < 0 or j >= MAX_COL or j < 0 or (i,j) in visited:
                return False
            if index == len(word) - 1 and board[i][j] == word[index]:
                return True
            if board[i][j] != word[index]:
                return False
            
            visited.add((i,j))
            res =  backtrack(i+1, j, index+1) or backtrack(i-1, j, index+1) or backtrack(i, j+1, index+1) or backtrack(i, j-1, index+1)
            visited.remove((i,j))
            return res

        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True

        return False
                

