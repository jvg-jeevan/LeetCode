class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
# nums list to store the count of 1s
        nums = []
# for each row in mat, append the number of 1s in row
        for row in mat:
            nums.append(row.count(1))
# get the maximum element and find the index and return
        maxi = max(nums)
        return [nums.index(maxi), maxi]
# # take 0th element as maxi
#         maxi = nums[0]
# # iterate through each element from 1st element
#         for i in range(1, len(nums)):
# # if element is greater than maxi then return [ind, element]
#             if nums[i] > maxi:
#                 return [i, nums[i]] 
# # if no greater element is found then return 1st element
#         return [0, maxi]