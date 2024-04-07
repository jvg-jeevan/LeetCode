from numpy import *
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = array(grid)
        nums = list(grid.flatten())
        result = []

# 1st element is duplicate number, 2nd element is missing number
        for x in range(1, len(nums)+1):
    # if count of element is greater than 1 then append to result
            if nums.count(x) > 1:
                result.append(x)
    # if element not in list then append to the result
            elif x not in nums:
                result.append(x)
# return the result
        return result