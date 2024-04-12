class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        # unpack the matrix into 1d list
        for row in matrix:
            arr.extend(row)
        # if element in arr then return True or else False
        if target in arr:
            return True
        else:
            return False