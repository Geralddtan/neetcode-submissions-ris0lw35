class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        l,r=0,ROW-1
        while l <= r:
            m = (r+l)//2
            if target > matrix[m][-1]:
                l = m+1
            elif target < matrix[m][0]:
                r = m-1
            else:
                break

        if target < matrix[m][0] or target > matrix[m][-1]:
            return False

        target_row = m
        l,r=0,COL-1
        while l <= r:
            m = (l+r)//2
            if target == matrix[target_row][m]:
                return True
            elif target > matrix[target_row][m]:
                l=m+1
            elif target < matrix[target_row][m]:
                r=m-1
        return False
            
        
        
        

        
