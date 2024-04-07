class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sumof = 0
        for i in range(1, len(nums)+1):
# if the lenght n is divided by index i then add square of that number to sum and return result
            if n%i == 0:
                sumof += (nums[i-1] ** 2)
        return sumof