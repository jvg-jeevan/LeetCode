class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        
# missing number can be found by subtracting expected sum and actual sum
        n = len(nums)
        act = (n * (n+1)) // 2
        expect = sum(nums)
        return act - expect