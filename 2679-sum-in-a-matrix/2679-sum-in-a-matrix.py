class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        
# res to store the resultant sum
        res = 0
        
# run until the first row is empty
        while nums[0]:
# matrix to store the maximum elements in each row
            matrix = []
# for each row in nums
            for row in nums:
# maxi store maximum element
                maxi = max(row)
# remove the maximum element form row
                row.remove(maxi)
# append the element maxi to matrix
                matrix.append(maxi)

# get the maximum element in matrix and update the res
            res += max(matrix)

# return res
        return res  