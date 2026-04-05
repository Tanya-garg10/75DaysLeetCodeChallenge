class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False