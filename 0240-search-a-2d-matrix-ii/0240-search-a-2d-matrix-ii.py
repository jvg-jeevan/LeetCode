class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# iterate through each row in matrix
        for row in matrix:
# if element is found in row return True 
            if target in row:
                return True
# if element not found in the matrix return False
        else:
            return False