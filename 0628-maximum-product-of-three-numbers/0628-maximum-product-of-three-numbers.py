class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
# sort the elements in the list
        nums.sort()
# get the max of product of elements
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
# (-1, -2, -3) for +ve elements 3 large numbers
# (0, 1, -1) for 1st two -ve elements(sorted) and the largest numbers