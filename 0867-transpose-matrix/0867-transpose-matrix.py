# from numpy import *
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
# can be done directly using numpy
        # arr = array(mat)
        # return arr.transpose()

# get the rows and cols of given matrix
        row = len(matrix)
        col = len(matrix[0])

# transpose = rows->cols and cols->rows
# create a transpose matrix with only zeros  
        res = [[0] * row for _ in range(col)]

# for each element in original matrix -> add that to the transpose element
        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]
        return res
# return the transpose matrix