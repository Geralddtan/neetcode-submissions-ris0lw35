class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        ## Find exact row
        bottom,top = 0, ROW-1
        while bottom <= top:
            row = (bottom+top)//2
            if target > matrix[row][-1]:
                bottom = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break

        if top < bottom:
            return False
        
        print(row)
        l,r = 0, COL
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
        
        
        

        
