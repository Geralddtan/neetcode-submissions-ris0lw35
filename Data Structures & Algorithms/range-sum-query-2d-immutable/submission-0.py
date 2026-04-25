class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == 0:
                    self.matrix[row][col] = matrix[row][col]
                else:
                    self.matrix[row][col] = self.matrix[row][col-1] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if col1 == 0:
            for row in range(row1, row2+1):
                res += self.matrix[row][col2]
        else:
            for row in range(row1, row2+1):
                res += self.matrix[row][col2] - self.matrix[row][col1-1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)