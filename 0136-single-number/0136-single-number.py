class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for i in nums:
        #     # return the number if count is zero
        #     if nums.count(i) == 1:
        #         return i

        res = nums[0]
        # take res as 1st element
        for x in range (1, len(nums)):
            # iterate through the loop 
            res ^= nums[x]
        return res
        # xor operation of same number results in zero
        # xor operation of zero and a number results in number
