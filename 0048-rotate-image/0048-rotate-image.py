class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
# to get the transpose of the matrix (takes 1 element from each row)
        matrix[:] = [list(row) for row in zip(*matrix)]
# for each row in matrix reverse the elements in the row alter in same
        for row in matrix:
            # row.reverse()
            row[:] = row[::-1]