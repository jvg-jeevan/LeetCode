# from numpy import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
# flattening the array can also be done using numpy
        # arr = array(matrix)
        # arr = arr.flatten()
        # arr.sort()
        # return arr[k-1]

        arr = []
        for row in matrix:
            arr.extend(row)
        
# convert the n-d matrix to 1-d array 

        arr.sort()
# sort the matrix and then the element at given index k
        return arr[k-1]