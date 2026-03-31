class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS-1
        row_target = None
        ans = False
        while low<=high:
            mid = (low+high)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_target = mid
                break
            elif matrix[mid][0]>target:
                high = mid-1
            else:
                low = mid+1
        if row_target is not None:
            low, high = 0, COLS-1
            while low<=high:
                mid = (low + high)//2
                if matrix[row_target][mid] == target:
                    ans = True
                    break
                elif matrix[row_target][mid] > target:
                    high-=1
                else:
                    low+=1
        return ans