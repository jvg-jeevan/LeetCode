class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
# get the sum of each list
        res = [sum(grid[i]) for i in range(len(grid))]
# return the maximum element index
        return res.index(max(res))