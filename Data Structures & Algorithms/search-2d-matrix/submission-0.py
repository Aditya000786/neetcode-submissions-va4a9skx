class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        row = None
        while low<=high:
            mid = (low + high)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                row = mid
                break
            elif matrix[mid][0]<target and matrix[mid][-1]<target:
                low = mid + 1
            elif matrix[mid][0]>target and matrix[mid][-1]>target:
                high = mid - 1
        if row is None:
            return False
        low, high = 0, len(matrix[mid])-1
        while low<=high:
            mid = (low+high)//2
            if matrix[row][mid]<target:
                low = mid + 1
            elif matrix[row][mid]>target:
                high = mid - 1
            else:
                return True
        return False