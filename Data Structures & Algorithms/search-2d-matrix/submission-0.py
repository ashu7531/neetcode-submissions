class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                return self.binarySearch(matrix[mid], target)
            if target > matrix[mid][-1]:
                start = mid + 1
            if target < matrix[mid][0]:
                end = mid - 1
        return False

    def binarySearch(self, rows, target):
        start = 0
        end = len(rows) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target == rows[mid]:
                return True
            if target > rows[mid]:
                start = mid + 1
            if target < rows[mid]:
                end = mid - 1
        return False
        