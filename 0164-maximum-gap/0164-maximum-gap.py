class Solution:
    def maximumGap(self, nums: list[int]) -> int:
# sort the nums list and remove the duplicate elements by converting to set
        nums = sorted(set(nums))
# initialize the difference as 0 
        res_diff = 0
# if length of nums is less than 2 the no difference
        if len(nums) <= 1:
            return res_diff
        
# iterate through each element and find the difference and max of both and assign to the res_diff and then return the result
        for i in range(len(nums)-1):
            res_diff = max(res_diff, (nums[i+1] - nums[i]))
        
        return res_diff
