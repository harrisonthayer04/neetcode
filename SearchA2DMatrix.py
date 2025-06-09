class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array: List[int], target: int):
            left  = 0
            right = len(array) - 1
            while left <= right:
                midpoint = (right + left) // 2
                if array[midpoint] > target:
                    right = midpoint - 1
                elif array[midpoint] < target:
                    left = midpoint + 1
                else:
                    return True
            return False  

        left  = 0 
        right = len(matrix) - 1

        
        # loop here
        while left <= right:
            matrix_midpoint = (left + right) // 2   
            if target > matrix[matrix_midpoint][-1]:
                left = matrix_midpoint + 1 
            elif target < matrix[matrix_midpoint][0]:
                right = matrix_midpoint - 1
            else:
                return binarySearch(matrix[matrix_midpoint], target)
        return False





# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 15
# Do binary seach to find the array
# 3 arrays
# Midpoint = array 2
# Is the target in the range of the current array
# If target is less then the range of the current array
    # Then move the right pointer
# If target is more than the range of the current array
    # Then move the left pointr
# If target is in the range of the current array
    # Binary search in the array

# Create a helper function that does binary search on an array
    # Return t/f 