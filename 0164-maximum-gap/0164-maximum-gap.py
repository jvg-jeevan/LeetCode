class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        res_diff = 0
        
        if len(nums) <= 1:
            return res_diff
        
        for i in range(len(nums)-1):
            res_diff = max(res_diff, (nums[i+1] - nums[i]))
        
        return res_diff
