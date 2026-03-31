class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        while top<=bottom:
            row = (top+bottom)//2
            if target<matrix[row][0]:
                bottom = row-1
            elif target>matrix[row][-1]:
                top = row+1
            else:
                break
        if not (top<=bottom):
            return False
        left, right = 0, len(matrix[0])
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]>target:
                right = mid-1
            elif matrix[row][mid]<target:
                left = mid+1
            else:
                return True
        return False