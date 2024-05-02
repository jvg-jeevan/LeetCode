class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        maximum = max(nums)

        
        if (0 - maximum) in nums:
            return maximum
        
        else:
            nums.remove(maximum)

            return self.findMaxK(nums)