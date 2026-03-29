class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW, MAX_COL = len(board), len(board[0])

        def backtrack(string, i, j, visited):
            if len(string) > len(word):
                return False
            if i >= MAX_ROW or j >= MAX_COL or i < 0 or j < 0 or (i,j) in visited:
                return False
            if string + board[i][j] == word:
                return True
        
            if board[i][j] == word[len(string)]:
                print(string, i, j, visited)
                string+=board[i][j]
                visited.add((i, j))
                return backtrack(string, i+1, j, visited.copy()) or backtrack(string, i, j+1, visited.copy()) or backtrack(string, i-1, j, visited.copy()) or backtrack(string, i, j-1, visited.copy())
            
        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                if board[row][col] == word[0]:
                    if backtrack("", row, col, set()):
                        return True
        
        return False
                
["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]

            
