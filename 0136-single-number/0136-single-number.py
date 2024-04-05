class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in nums:
        #     # return the number if count is zero
        #     if nums.count(i) == 1:
        #         return i

        res = nums[0]
        for x in range (1, len(nums)):
            res ^= nums[x]
        return res