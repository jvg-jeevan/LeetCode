class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
# res to store the count of negative
        res = 0
# take each row in grid
        for row in grid:
# for each num in row
            for num in row:
# if num < 0 increment res
                if num < 0:
                    res += 1
# return res
        return res